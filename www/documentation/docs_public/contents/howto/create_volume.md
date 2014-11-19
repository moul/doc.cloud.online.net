---
title: Attach and detach a volume
template: article.jade
position: 3
---

This page shows how to attach and detach additional volumes to an existing server.

> <strong>Requirements</strong>
>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)
- You have a [server](/howto/create_instance.html)

Each server can have at most 16 volumes, including the root volume. <br/>
You can select the type of disk to host your volumes from two technologies:

- LSSD (Local solid state drive), to deliver fast disk I/O (Local solid state drive)
- LHDD (Local spinning disk), use for moderate read/write access.

LSSD and LHDD volumes are teleported close to your server.

When you start a server for the first time, your volume files are downloaded from the volumes store to the local storage devices (LHDD or LSSD).

Each time you start or stop a server, the volumes are downloaded or uploaded to the volumes store.
The larger the amount of data to transfer, the longer the upload or download duration.

We work constantly on optimizing the transfer time of local storage devices to the volumes store.

There are two steps to attach a volume to an existing server

- [Create a new volume](/howto/create_volume.html#step-1-create-a-new-volume)
- [Attach an existing volume to your instance](/howto/create_volume.html#step-2-attach-an-existing-volume-to-your-instance)
- [Moun additional volumes](/howto/create_volume.html#step-3-mount-additional-volumes)

<strong>Important</strong>: Server must be powered off to attach or detach a volume.

## Attach a volume to an existing server

In the Control Panel, click "Volumes" in the compute section.

### Step 1 - Create a new volume

Click the "Create Volume" button.<br/>
You will land on the volume-creation page where you must input basic information for your volume:

- The name of your volume
- The volume type - LSSD (Local solid state drive) or LHDD (Local spinning disk)
- The size in Go

![Create new volume](../../images/create_new_volume.png "Create new volume")

### Step 2 - Attach an existing volume to your instance

In the servers page, click on the server you want to attach a volume to.

![Create new volume](../../images/attach_volume.png "Create new volume")

On the server detail page click "Attach an existing volume" and select the volume to attach in the list.

<strong>Important</strong>: To detach the volume, click the Detach button.

## Step 3 - Mount additional volumes

### Format additional volumes

If the new volume has never been formatted, you need to format the volume using `mkfs` before you can mount it.

For instance, the following command creates an `ext4` file system on the volume:

```
root@c1-X-Y-Z-T:~# mkfs -t ext4 /dev/nbd1
mke2fs 1.42.9 (4-Feb-2014)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
610800 inodes, 2441406 blocks
122070 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=2503999488
75 block groups
32768 blocks per group, 32768 fragments per group
8144 inodes per group
Superblock backups stored on blocks:
  32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done
Writing inode tables: done
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done
```

### Mount additional volumes manually

To mount the device manually as /mnt/data, run the following commands:

```
root@c1-X-Y-Z-T:~# mkdir -p /mnt/data
root@c1-X-Y-Z-T:~# mount /dev/nbd1 /mnt/data
root@c1-X-Y-Z-T:~# ls -la /mnt/data/
total 24
drwxr-xr-x 3 root root  4096 Jan  1 00:07 .
drwxr-xr-x 3 root root  4096 Jan  1 00:07 ..
drwx------ 2 root root 16384 Jan  1 00:07 lost+found
```

### Mount additional volumes with fstab (automatic mount)

To mount additional volumes automatically, you have to reference your devices in the `/etc/fstab` file.<br />
`/etc/fstab` references all devices to mount when they are connected.

For instance to mount `/dev/nbd1` device automatically to the `/mnt/data` directory, the `/etc/fstab` has the following content:

```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>

/dev/nbd1 /mnt/data auto  defaults,nobootwait,errors=remount-ro 0 2
```

The configuration above mounts the /dev/nbd1 device to the `/mnt/data` directory with fstab default option and `nobootwait`.<br />
`nobootwait` is set to prevent boot problems in the case your volume is not yet downloaded to the local storage.

Create the /mnt/data directory if it doesn't exist.

```
root@c1-X-Y-Z-T:~# mkdir -p /mnt/data
```

To check devices are mounted properly, run the `mount -a` command to mount all devices.

<strong>Important</strong>: On the next server boot, your volumes will be mount automatically.

Now run the `df -h` command, this command will list all your devices and where they are mounted:

```
root@c1-X-Y-Z-T:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/nbd0        23G  420M   22G   2% /
none           1010M   36K 1010M   1% /dev
none            203M   80K  203M   1% /run
none            5.0M     0  5.0M   0% /run/lock
none           1012M     0 1012M   0% /run/shm
none            100M     0  100M   0% /run/user
/dev/nbd1       9.2G  149M  8.6G   2% /mnt/data
```