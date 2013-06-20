---
title: Connect to a block device manually
template: article.jade
position: 3
---

This page shows you how to connect a block device manually.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)
- You have a running [server](/howto/create_instance.html)
- Your server has additional [volumes](/howto/create_instance.html#step-3-add-storage)

When you create a server with additional storage, the connection to a block device is automatic at the server boot.

If you want to avoid this behavior and connect additional block device manually, execute the following command on your server `echo manual > /etc/init/nbd-add-extra-volumes.override`

There are three steps to connect a block device manually

- [Identify NBD server and port](/advanced/nbd.html#step-1-identify-nbd-server-and-port)
- [Connect to a block device](/advanced/nbd.html#step-2-connect-to-a-block-device)
- [Format and mount the volume](/advanced/nbd.html#step-3-format-and-mount-the-volume)

<strong>Important</strong>: The maximum number of volumes attach to C1 server is limited at 15 devices.<br/>

### Step 1 - Identify NBD server and port

The NBD client requires the IP address and the port number of our NBD server exporting your volume.<br/>
These settings are available from your server details page on the control panel

![Server details](../../images/server_details.png "Server details")

The above picture shows the IP address and the port number required to export the volume in our example.

You can also use "server metadata" which give you a lot of information.<br/>
Execute the following command on your server to display server metadata

```
[root]$metadata
NAME=myc1
TAGS=1
TAGS_0=test
STATE_DETAIL=booted
PUBLIC_IP=DYNAMIC ID ADDRESS
PUBLIC_IP_DYNAMIC=True
PUBLIC_IP_ID=9915ace8-2729-4289-b962-f6a2f94d44a0
PUBLIC_IP_ADDRESS=212.47.236.31
SSH_PUBLIC_KEYS=1
SSH_PUBLIC_KEYS_0=KEY
SSH_PUBLIC_KEYS_0_KEY='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwtTLiaKl+YPV0LjN/DJtS6hYOAEEXqAS1O5z8ft61da+3sG/kd3j9ONiepugG6sanGKRAMvx652OIZDgWbzEC40/7shAoxxbiFXBj3VgPCoKXCNLtTla4nx9hR/Xstzfm6k3/mODiioWV+TwWimM9SRo5ihwF09BhLw4sfTchtUxlLrW6pv0o4ykBPMC90yJl5KrB+7QKWaedbUYwBkXHNDDOTpBawJppp3hcfPhJjZrCk4NCdNsRhmhwaKMPNmx37hBs+Wu3Y2aAbHd4tAsQAc646/E6Xlipll8IzkNaH7PGYLhMmHB9FXI6gavi0UF12OC7abzm+MiLDOzRBx1'
PRIVATE_IP=10.1.0.31
VOLUMES=1 0
VOLUMES_1=NAME EXPORT_URI VOLUME_TYPE SERVER ORGANIZATION ID SIZE
VOLUMES_1_NAME=data_vol
-> VOLUMES_1_EXPORT_URI=nbd://10.1.0.44:4321
VOLUMES_1_VOLUME_TYPE=l_hdd
VOLUMES_1_SERVER=ID NAME
VOLUMES_1_SERVER_ID=838271d7-9744-4b3e-b29c-1c38c7c435e8
VOLUMES_1_SERVER_NAME=myc1
VOLUMES_1_ORGANIZATION=ecc1c86a-1122-43a7-9c0a-77e3123456789
VOLUMES_1_ID=965b38e6-b3bf-466c-a13c-b2004f37214a
VOLUMES_1_SIZE=100000000000
VOLUMES_0=NAME EXPORT_URI VOLUME_TYPE SERVER ORGANIZATION ID SIZE
VOLUMES_0_NAME='Ubuntu Trusty (14.04) on SSD 2014.07.15'
VOLUMES_0_EXPORT_URI=nbd://10.1.0.44:4320
VOLUMES_0_VOLUME_TYPE=l_ssd
VOLUMES_0_SERVER=ID NAME
VOLUMES_0_SERVER_ID=838271d7-9744-4b3e-b29c-1c38c7c435e8
VOLUMES_0_SERVER_NAME=myc1
VOLUMES_0_ORGANIZATION=ecc1c86a-1122-43a7-9c0a-77e3123456789
VOLUMES_0_ID=b741de3c-6bf7-4e07-b432-baadcef606a3
VOLUMES_0_SIZE=20000000000
ORGANIZATION=ecc1c86a-1122-43a7-9c0a-77e3123456789
ID=838271d7-9744-4b3e-b29c-1c38c7c435e8
```

- VOLUMES_0 / VOLUMES_0_* always match the root volume of the server. Server connects and mount it automatically at boot time

- VOLUMES_[1-15] / VOLUMES_[1-15]_* is an additional volume(s) attach to the server.

`VOLUMES_[1-15_EXPORT_URI=nbd://10.1.0.44:4321` this entry shows NBD server IP address and the port number of our NBD server exporting your volume.

### Step 2 - Connect to a block device

An instance of the NBD client must be started for each block device to import.

For instance: 
```
[root]$nbd-client 10.1.0.44 4321 /dev/nbd1
Negotiation: ..size = 9536MB
bs=1024, sz=9999998976 bytes

[root]$fdisk -l -u /dev/nbd1
Disk /dev/nbd1: 100.0 GB, 99999997952 bytes
255 heads, 63 sectors/track, 12157 cylinders, total 195312496 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

```

In the above example, `nbd-client 10.1.2.21 4129 /dev/nbd1` connects to the NBD server.<br/>
The output of `fdisk -l -u /dev/nbd1` command shows that the block device `/dev/nbd1` is attached to the server with success.

### Step 3 - Format and mount the volume

In the previous step, the new volume was attached to `/dev/nbd1`.

If the new volume has never been formatted, you need to format the volume using `mkfs` before you can mount it.

For instance, the following command creates an `ext4` file system on the volume.

 ```
[root]$mkfs -t ext4 /dev/nbd1
mke2fs 1.42.9 (4-Feb-2014)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
6111232 inodes, 24414062 blocks
1220703 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=0
746 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks:
  32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
  4096000, 7962624, 11239424, 20480000, 23887872

Allocating group tables: done
Writing inode tables: done
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information:
done
```

Then, to mount the device as /mnt/data, run the following commands.

```
[root]$mkdir -p /mnt/data
[root]$mount /dev/nbd1 /mnt/data
[root]$ls -la /mnt/data/
total 24
drwxr-xr-x 3 root root  4096 Jan  1 00:07 .
drwxr-xr-x 3 root root  4096 Jan  1 00:07 ..
drwx------ 2 root root 16384 Jan  1 00:07 lost+found
```

Now run the `df -h` command, this command will list all your devices and where they are mounted

```
[root]$df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/nbd0        19G  614M   17G   4% /
none           1011M   36K 1011M   1% /dev
none            203M   92K  203M   1% /run
none            5.0M     0  5.0M   0% /run/lock
none           1013M     0 1013M   0% /run/shm
none            100M     0  100M   0% /run/user
/dev/nbd1        92G  188M   87G   1% /mnt/data

```
