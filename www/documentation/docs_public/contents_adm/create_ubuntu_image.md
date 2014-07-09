---
title: Create your image from scratch
template: article.jade
position: 2
---

This page shows you how to create a new image from scratch.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)
- You have a server starts with an additional volume [Provisioning your server](/howto/create_instance.html)

There are two steps to create a new image from scratch

### Step 1 - Install deboostrap

```
apt-get install deboostrap
```

### Step 2 - Creation of the template

```
DEBOOTSTRAP_DIR=/tmp/ubuntu-tpl/
PKGS_INCLUDE='ssh,rsyslog,vim-tiny,nano,less,man-db,net-tools,iputils-ping,whiptail,wget,nbd-client,xnbd-client,isc-dhcp-client,curl,sudo,iptables,ntp'

mkdir $DEBOOTSTRAP_DIR
debootstrap --arch armhf --variant=minbase --components main,universe --include $PKGS_INCLUDE trusty $DEBOOTSTRAP_DIR

for i in {1..6}
do
  echo manual > $DEBOOTSTRAP_DIR/etc/init/tty$i.override
done

FILES_TO_COPY="/etc/init/ttyS0.conf /etc/init/ssh-keys.conf"
FILES_TO_COPY+=" /etc/init/nbd-root-preserve-client.conf"
FILES_TO_COPY+=" /etc/init/nbd-root-disconnect.conf"
FILES_TO_COPY+=" /sbin/nbd-disconnect-root"
FILES_TO_COPY+=" /etc/default/rcS"
FILES_TO_COPY+=" /etc/ntp.conf"
FILES_TO_COPY+=" /etc/hosts"
FILES_TO_COPY+=" /etc/sysctl.conf"
FILES_TO_COPY+=" /etc/network/interfaces.d/network"
FILES_TO_COPY+=" /usr/local/bin/metadata"
FILES_TO_COPY+=" /usr/local/bin/metadata-json"

for FILE in ${FILES_TO_COPY}
do
  cp ${FILE} ${DEBOOTSTRAP_DIR}${FILE}
done

nbd-client `curl http://169.254.42.42/conf | grep VOLUMES_1_EXPORT_URI | sed 's#VOLUMES_1_EXPORT_URI=nbd://##g' | tr ':' ' '` /dev/nbd1
mkfs.ext4 /dev/nbd1

IMG_MOUNTPOINT=/mnt/ubuntu-rootfs/

mount /dev/nbd1 $IMG_MOUNTPOINT

rsync -aHKXxA --progress $DEBOOTSTRAP_DIR $IMG_MOUNTPOINT
```

### Embedded scripts source
#### /etc/init/ttyS0.conf
```
# ttyS0 - getty
#
# This service maintains a getty on ttyS0 from the point the system is
# started until it is shut down again.

start on stopped rc RUNLEVEL=[2345] and (
            not-container or
            container CONTAINER=lxc or
            container CONTAINER=lxc-libvirt)

stop on runlevel [!2345]

respawn
exec /sbin/getty -L ttyS0 9600 vt102
```

#### /etc/init/ssh-keys.conf
```
# ssh-keys
description "generate and fetch needed ssh keys"
author "Yann LEGER <yleger@ocs.online.net>"

start on started ssh

task

script
    if [ ! -f /etc/ssh/ssh_host_rsa_key ]
    then
        ssh-keygen -t rsa -b 4096 -N '' -f /etc/ssh/ssh_host_rsa_key
        ssh-keygen -t dsa -N '' -f /etc/ssh/ssh_host_dsa_key
        ssh-keygen -t ecdsa -N '' -f /etc/ssh/ssh_host_ecdsa_key
        ssh-keygen -t ed25519 -N '' -f /etc/ssh/ssh_host_ed25519_key
    fi

    if [ ! -f /root/.ssh/authorized_keys ]
    then
        mkdir -p /root/.ssh/
    fi

    for i in 1 1 1 2 2 2 3 4 5 6 7 8 9 10 20 30 40 50 60 100 100 100 100 100
    do
        wget -q http://169.254.42.42/conf -O - | grep SSH_PUBLIC_KEYS_'.*'_KEY | cut -d'=' -f 2- | tr -d \' > /root/.ssh/authorized_keys
    if [[ -s /root/.ssh/authorized_keys ]]
    then
            break
    fi
    sleep $i
    done
end script
```

#### /etc/init/nbd-rootfs.conf
```
description "NBD root init script"
author "Yann LEGER <yleger@ocs.online.net>"

start on ((filesystem and runlevel [!06])
          or runlevel PREVLEVEL=S)
stop on starting rc RUNLEVEL=[06]

post-stop script
    if [ -x /sbin/nbd-disconnect-root ]; then
        /sbin/nbd-disconnect-root&
    fi
end script
```

#### /sbin/nbd-disconnect-root
```
#!/bin/sh
# Thanks to the LTSP project
# If the root /dev/nbd0 device is unmounted on shutdown then nbd read
# errors occur, and if it isn't, then # the nbd-server process on the server
# doesn't terminate.
# Called by init scripts on reboot or shutdown.

case "$RUNLEVEL" in
    0)
        key="o"
        command="poweroff -f"
        ;;
    6)
        key="b"
        command="reboot"
        ;;
    *)
        echo "nbd-disconnect should only be called by initscripts on
reboot/shutdown." >&2
        exit 1
        ;;
esac

disconnect() {
    # Stop trapping
    trap - 0 HUP INT QUIT KILL SEGV PIPE TERM

    # ltsp-client-core.upstart needs "console output" to show stderr
    echo "nbd-disconnect executing: $command" >&2
    # Cache the command in order to use it after nbd-client disconnects
    $command --version >/dev/null 2>&1
    nbd-client -d "$root"
    $command
    # Hopefully this should never be reached
    echo "$key" > /proc/sysrq-trigger
}

# Disconnect swap nbd devices first
while read device etc; do
    case "$device" in
        /dev/nbd[0-9])
            swapoff "$device"
            nbd-client -d "$device"
            ;;
        /dev/mapper/swap[0-9])
            nbd_device=$(cryptsetup status "$device" | awk '/device:/{print
$2}')
            swapoff "$device"
            cryptsetup remove "$device"
            case "$nbd_device" in
                /dev/nbd[1-9])
                    nbd-client -d "$nbd_device"
                    ;;
            esac
            ;;
    esac
done < /proc/swaps

# If we're not using an nbd root, exit
unset root
for param in $(cat /proc/cmdline); do
    case "$param" in
        root=/dev/nbd[0-9])
            root="${param#root=}"
            ;;
    esac
done
test -n "$root" || exit 0
 
trap "disconnect" 0 HUP INT QUIT KILL SEGV PIPE TERM
sync
# Give up to 5 seconds for other services to be called.
# If they finish before that time, process termination will start, and the trap
# will be called.
sleep 5
```

#### /etc/sysctl.conf
```
###################################################################
# The min_free_kbytes setting
vm.min_free_kbytes=65536
```

#### /etc/network/interfaces.d/network
```
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp
```

#### /etc/hosts
```
127.0.0.1   localhost
::1     localhost ip6-localhost ip6-loopback
ff02::1     ip6-allnodes
ff02::2     ip6-allrouters
```

#### /etc/ntp.conf
```
# /etc/ntp.conf, configuration for ntpd; see ntp.conf(5) for help

driftfile /var/lib/ntp/ntp.drift


# Enable this if you want statistics to be logged.
#statsdir /var/log/ntpstats/

statistics loopstats peerstats clockstats
filegen loopstats file loopstats type day enable
filegen peerstats file peerstats type day enable
filegen clockstats file clockstats type day enable

# Specify one or more NTP servers.
server 10.1.31.38

# Use Ubuntu's ntp server as a fallback.
server ntp.ubuntu.com

# Access control configuration; see /usr/share/doc/ntp-doc/html/accopt.html for
# details.  The web page <http://support.ntp.org/bin/view/Support/AccessRestrictions>
# might also be helpful.
#
# Note that "restrict" applies to both servers and clients, so a configuration
# that might be intended to block requests from certain clients could also end
# up blocking replies from your own upstream servers.

# By default, exchange time with everybody, but don't allow configuration.
restrict -4 default kod notrap nomodify nopeer noquery
restrict -6 default kod notrap nomodify nopeer noquery

# Local users may interrogate the ntp server more closely.
restrict 127.0.0.1
restrict ::1

# Clients from this (example!) subnet have unlimited access, but only if
# cryptographically authenticated.
#restrict 192.168.123.0 mask 255.255.255.0 notrust


# If you want to provide time to your local subnet, change the next line.
# (Again, the address is an example only.)
#broadcast 192.168.123.255

# If you want to listen to time broadcasts on your local subnet, de-comment the
# next lines.  Please do this only if you trust everybody on the network!
#disable auth
#broadcastclient
```

#### /usr/local/bin/metadata-json
```
#!/bin/sh

code=0
while [ $code -ne 200 ]
do
    response=$(curl --silent --write-out "\n%{http_code}\n" http://169.254.42.42/conf?format=json)
    code=$(echo "$response" | sed -n '$p')
    body=$(echo "$response" | sed '$d')
done

echo "$body"
```

#### /usr/local/bin/metadata
```
#!/bin/sh

code=0
while [ $code -ne 200 ]
do
    response=$(curl --silent --write-out "\n%{http_code}\n" http://169.254.42.42/conf)
    code=$(echo "$response" | sed -n '$p')
    body=$(echo "$response" | sed '$d')
done

echo "$body"
```