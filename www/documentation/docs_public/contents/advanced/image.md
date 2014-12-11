---
title: Create an image from scratch
template: article.jade
position: 4
---

This page shows how to create a new image from scratch.
This process consists in building a root filesystem in an extra volume of one of your servers.

The following procedure will create an Ubuntu based image from scratch.

> <strong>Requirements</strong>
>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)
- You have an additional volume attached to your server [Provisioning your server](/howto/create_instance.html)

When you create a server you have to select a base image.
If you create your own base image, you can customize more deeply.

There are three steps to create a new image from scratch:

- [Create the root filesystem](/advanced/image.html#step-1-create-the-root-filesystem)
- [Create an image from a snapshot](/advanced/image.html#step-4-create-an-image-from-snapshot)
- [Create a new server with your image](/advanced/image.html#step-5-create-a-new-server-with-your-image)

### Step 1 - Create the root filesystem

It is possible to create a root filesystem in two ways:

- using [Deboostrap](/advanced/image.html#create-the-root-filesystem-using-deboostrap)
- using [Docker](/advanced/image.html#create-the-root-filesystem-using-docker) (recommended)

#### Create the root filesystem using Deboostrap

> <strong>Requirements</strong>
>
- You are running a Debianish system on your server

Connect to your server and execute the following command:

```
apt-get update
apt-get install debootstrap
```

Debootstrap is used to install Debian-like systems without using an installation disk.
This way, you can create a fully functioning minimal installation.

Then, we create a bash script to build our image.

Each part of the script is described line by line.

```
#!/bin/bash

# Name  of  the  bootstrap  script variant to use.
# Currently, the variants supported are minbase,
# which  only  includes  essentialpackages  and  apt;  buildd,
# which installs the build-essential
# packages  into  TARGET;  and  fakechroot,  which  installs   the
# packages  without  root  privileges.   Finally  there is variant
# scratchbox, which is for creating targets for scratchbox  usage.
#  The  default,  with no --variant=X argument, is to create a base
VARIANT=minbase

# The system architecture, C1 server architecture type is armhf
ARCH=armhf

# Use packages from the listed components of the archive.
COMPONENTS=main,universe

# The volume to boostrap the system
DEBOOTSTRAP_DIR=/mnt/ubuntu-tpl/

# The list of packages included in the system

PKGS_INCLUDE='ca-certificates, cron, curl, iptables, iputils-ping, isc-dhcp-client, less,libnss-myhostname, man-db, nano, nbd-client, net-tools, ntp, ntpdate, rsyslog, ssh, sudo, vim, wget, whiptail, xnbd-client'

MIRROR=http://mirror.cloud.online.net/ubuntu-ports/

DEVICE=/dev/nbd1

# Check if directory DEBOOTSTRAP_DIR exists
if [ ! -d "$DEBOOTSTRAP_DIR" ]; then
  mkdir -p $DEBOOTSTRAP_DIR
fi

# Format /dev/nbdx volume


# Format & Mount /dev/nbdx in #DEBOOTSTRAP_DIR
if [ ! `mountpoint -q $DEBOOTSTRAP_DIR` ]; then
  mkfs.ext4 $DEVICE
  mount $DEVICE $DEBOOTSTRAP_DIR
fi

# Bootstrap a basic Ubuntu trusty system
 debootstrap --arch $ARCH --variant=$VARIANT --components "$COMPONENTS" --include "$PKGS_INCLUDE" trusty $DEBOOTSTRAP_DIR "$MIRROR"

for i in {1..6}
do
  echo manual > $DEBOOTSTRAP_DIR/etc/init/tty$i.override
done

# The list of files required to copy on the template

# Upstart job - Maintains a getty on ttyS0
FILES_TO_COPY="/etc/init/ttyS0.conf"

# Upstart job - Fetches ssh-keys associated with your account in `/root/.authorized_keys`
FILES_TO_COPY+=" /etc/init/ssh-keys.conf"

# Upstart job - Preserves the NBD client process on shutdown
FILES_TO_COPY+=" /etc/init/nbd-root-preserve-client.conf"

# Upstart job - Gracefully umount and disconnect root volume
FILES_TO_COPY+=" /etc/init/nbd-root-disconnect.conf"

# Upstart job - Connects additional volumes to NBD server
FILES_TO_COPY+=" /etc/init/nbd-add-extra-volumes.conf"

# Upstart job - Synchronizes kernel modules
FILES_TO_COPY+=" /etc/init/sync-kernel-modules.conf"

# This script is required by `/nbd-root-disconnect.conf` to disconnect root volume gracefully.
FILES_TO_COPY+=" /usr/sbin/nbd-disconnect-root"

# Variables for the behavior of boot scripts
FILES_TO_COPY+=" /etc/default/rcS"

# ntpd service configuration with appropriate NTP servers
FILES_TO_COPY+=" /etc/ntp.conf"

# Map some hostnames to IP addresses before DNS can be referenced.
FILES_TO_COPY+=" /etc/hosts"

# Kernel options related on C1 server
FILES_TO_COPY+=" /etc/sysctl.conf"

# Network interfaces configuration
FILES_TO_COPY+=" /etc/network/interfaces"

# Executable which synchronizes kernel modules
FILES_TO_COPY+=" /usr/sbin/oc-sync-kernel-modules"

# Executable which retrieves server metadata (TEXT)
FILES_TO_COPY+=" /usr/local/bin/oc-metadata"

# Executable which retrieves server metadata (JSON)
FILES_TO_COPY+=" /usr/local/bin/oc-metadata-json"

# DHCP hook
FILES_TO_COPY+=" /etc/dhcp/dhclient-exit-hooks.d/hostname"

# Copy files above in the appropriate directory
for FILE in ${FILES_TO_COPY}
do
  cp ${FILE} ${DEBOOTSTRAP_DIR}${FILE}
done

umount $DEBOOTSTRAP_DIR
```

<strong>Important</strong>: All scripts source are available on the official image.

Execute the script above on your server `chmod +x ./image_creation.sh && ./image_creation.sh`.<br/>
Finally, stop your server.

#### Create the root filesystem using Docker

> <strong>Requirements</strong>
>
- Your server is running the Docker image from the InstantApps

Connect to your server and clone the hello-world repository:

```
git clone https://github.com/online-labs/image-helloworld.git
cd image-helloworld
```

It is composed of two files:

* a `Makefile`, which contains variables describing your image (version, name, title, description, URL)
* a `Dockerfile`, which tells how your image is built ([Dockerfile Reference](https://docs.docker.com/reference/builder/))

The image can then be built on `/dev/nbd1`:

```
make install_on_disk
```

### Step 3 - Create a snapshot

At this point the extra volume contains a valid Ubuntu root filesystem.
We must now transform this volume into a snapshot.

Once you server is powered off, from the servers page, select the server you created the image with.<br/>
Click the "Snapshot" button on the extra volume (in our example "volume_to_backup" - /dev/nbd1).

![Volume snapshot](../../images/volume_snapshot.png "Volume snapshot")

### Step 4 - Create an image from snapshot

In the Control Panel, click "Volumes" in the compute section.<br/>
On this page, select the snapshot containing your rootfs and click "Create an image from snapshot".

### Step 5 - Create a new server with your image

Create a new server and choose your image in "My images" section.

Your server will start on your own "from scratch" image.
