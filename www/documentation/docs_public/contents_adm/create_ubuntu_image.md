---
title: Create your image from scratch
template: article.jade
position: 2
---

```sh
## Creation of the template
DEBOOTSTRAP_DIR=/tmp/ubuntu-tpl/
PKGS_INCLUDE='ssh,rsyslog,vim-tiny,nano,less,man-db,net-tools,iputils-ping,whiptail,wget'

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

for FILE in ${FILES_TO_COPY}
do
  cp ${FILE} ${DEBOOTSTRAP_DIR}${FILE}
done


## Clone of the template
IMG_MOUNTPOINT=/mnt/ubuntu-rootfs/

nbd-client 10.1.4.153 4161 /dev/nbd1
mkfs.ext4 /dev/nbd1

mkdir $IMG_MOUNTPOINT
mount /dev/nbd1 $IMG_MOUNTPOINT
rsync -aHKXxA --progress $TMP_DIR $IMG_MOUNTPOINT

```

# Embedded scripts source
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
        wget -q http://169.254.42.42/conf -O - | grep SSH_PUBLIC_KEYS_'.*'_KEY | cut -d'=' -f 2 | tr -d \' > /root/.ssh/authorized_keys
    fi
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
