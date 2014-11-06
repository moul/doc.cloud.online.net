---
title: Provisioning your server
template: article.jade
position: 2
---

This page shows how to launch and connect to your servers.

> <strong>Requirements</strong>
>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)

Each server that you create is a physical server dedicated for you, there is no virtualization.

After you've launched your server, you can connect to it as root and use it as you wish.

There are five steps to provision a new server

- [Name & tag your server](/howto/create_instance.html#step-1-name-tag-your-server)
- [Choose your image](/howto/create_instance.html#step-2-choose-your-image)
- [Add storage](/howto/create_instance.html#step-3-add-storage)
- [Start the server](/howto/create_instance.html#step-4-start-your-server)
- [Mount additional volumes (Optional)](/howto/create_instance.html#mount-additional-volumes)

<strong>Important</strong>: Your SSH public keys are fetched during the boot process.

If you add them after your server is booted, they will *not* be added to your `authorized_keys` file.

If you do not want the keys to be downloaded during the next boot, execute the following command on your server:
```
root@c1-X-Y-Z-T:~# echo manual > /etc/init/ssh-keys.override
```

## Server creation

Before starting, click the "Create Server" button in the control panel.

![Control Panel](../../images/dashboard.png "Control Panel")

### Step 1 - Name & tag your server

You will land on the server-creation page where you must input basic information for your server:

- The name of your server
- The tag you want to assign to it (Optional). Tags let you organize your servers, you can assign any tag to each server.

![Create server basic information](../../images/server_basic_information.png "Create server basic information")

### Step 2 - Choose your image

After inputting your server basic information, you have to choose a starting image for your server.

You can choose this image from three sources:

- <strong>Marketplace</strong>: We provide an up-to-date list of linux distributions.

- <strong>My images</strong>: You can populate your own list of server templates. [See also Create your own image](/howto/create_image.html)

- <strong>Snapshots</strong>: You can recover a server from a previously saved state. [See also Backup your data with snapshots](/howto/create_snapshot.html)

![Create server image](../../images/server_image.png "Create server image")

### Step 3 - Add storage

A simple solution to increase the storage for your servers is to add extra volumes.

You can add extra storage to your server.
Added storage can be an existing volume or new volume.

You can select the type of disk to host your volumes from two technologies:

- LSSD (Local solid state drive) to deliver fast disk I/O.
- LHDD (Local spinning disk), use for moderate read/write access.

![Create server volumes](../../images/server_volume.png "Create server volumes")

### Step 4 - Start your server

Click the "Create Server" button. This action starts your server.
In a few seconds, your server will be ready to use.

## Log into your server

When your server is running, you can see the server's IP address in the server list on the control panel.

### For OSX and Linux

On a Mac or Linux computer, open your terminal program and in the shell just type the following command:

```
john@localhost:~$ ssh root@<your_server_ip>
```

Allow the connection to the host:

```sh
The authenticity of host 'myhost.ext (212.47.226.35)' can't be established.
RSA key fingerprint is 4f:ba:65:cf:14:64:a7:1e:b6:07:7c:00:71:95:21:fa.
Are you sure you want to continue connecting (yes/no)?
```

Well done, you are now logged into your server!

### For Windows

On Windows, you will need a small application named PuTTy, an SSH client.
You can download putty [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

Once you have downloaded PuTTY, just start the program.

- Fill the "Hostname" field with your server's IP address
- In the left-side menu, under Connection, expand the SSH sub-category
- Select the Auth sub-category and click the "Browse" button
- Select the private key file you generated previously
- Return in the Session category and click the "Open" button

![Import your SSH key on Putty](../../images/puttygen-3.png "Import your SSH key on Putty")

You are now logged into your server from Windows!

## Mount additional volumes

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

Then, to mount the device as /mnt/data, run the following commands:

```
root@c1-X-Y-Z-T:~# mkdir -p /mnt/data
root@c1-X-Y-Z-T:~# mount /dev/nbd1 /mnt/data
root@c1-X-Y-Z-T:~# ls -la /mnt/data/
total 24
drwxr-xr-x 3 root root  4096 Jan  1 00:07 .
drwxr-xr-x 3 root root  4096 Jan  1 00:07 ..
drwx------ 2 root root 16384 Jan  1 00:07 lost+found
```

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
