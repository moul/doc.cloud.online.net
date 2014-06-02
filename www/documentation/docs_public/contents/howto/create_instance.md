---
title: Provisioning your server
template: article.jade
position: 1
---

This page shows you how to launch and connect to your servers.

Requirements

- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)

Each server that you create is a physical server dedicated for your personal use.<br/>
After you've launched your server, you can connect and use it.

There are five steps to provision a new server

- Name & tag your server
- Choose your image
- Add storage
- Start the server
- Mount additional volumes (Optional)

## Server creation

Before starting, click the "Create Server" button in the control panel.

![Control Panel](../../images/dashboard.png "Control Panel")

### Step 1 - Name & tag your server

You will land on the server-creation page where you must input basic information for your server:

- The name of your server
- The tag you want to assign on it (Optional). Tags let you organize your servers, you can assign any tag to each server

![Create server basic information](../../images/server_basic_information.png "Create server basic information")

### Step 2 - Choose your image

After inputing your server basic information, you have to choose a starting image for your server.

You can choose this image from three sources:

- <strong>Marketplace</strong>: We provide an up-to-date list of linux distributions.

- <strong>My images</strong>: You can populate your own list of server templates. [See also Create your own image](/howto/create_image.html)

- <strong>Snapshots</strong>: You can recover a server from a saved previous state. [See also Backup your data with snapshots](/howto/create_snapshot.html)

![Create server image](../../images/server_image.png "Create server image")

### Step 3 - Add storage

You can add extra storage to your server. Added storage can be an existing volume or new volume.

You can select the type of disk to host your volumes from two technologies:

- LSSD (Local solid state drive) to deliver fast disk I/O (Local solid state drive) 
- LHDD (Local spinning disk), use for moderate read/write access.

![Create server volumes](../../images/server_volume.png "Create server volumes")

Currently, we limit LSSD to XXGiB and LHDD to XXGiB.

### Step 4 - Start your server

Click the "Create Server" button. This action starts your server. In a few seconds, your server will be ready to use.

## Log into your server

When your server is running, you can see the server's IP adress in the server list on the control panel

### For OSX and Linux

On a Mac or Linux computer, open your terminal program and in the shell just type the following command:

```
[john]$ssh root@<your_server_ip>
```

Allow the connection to the host<br/>
```sh
The authenticity of host 'myhost.ext (212.47.226.35)' can't be established.
RSA key fingerprint is 4f:ba:65:cf:14:64:a7:1e:b6:07:7c:00:71:95:21:fa.
Are you sure you want to continue connecting (yes/no)?
```

Well done, you are now logged into your server!

### For Windows

On Windows, you will need a small apllication named PuTTy, an SSH client. You can download putty [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
Once you have installed PuTTY, just start the program.

Fill the "Hostname" field with your server's IP address and click "Connect". You are now logged into your server from Windows!

## Mount additional volumes

A simple solution to increase the storage for your servers is to add extra volumes.

You need to export and mount these extra volumes manually.
We use NBD to connect your block device. [Read more about NBD here]()


![Server details](../../images/server_details.png "Server details")

In the server details are displayed the IP address and the port number required to export your volume.

### Step 1 - Connect to a block device

An instance of the NBD client must be started for each block device to import.

The NBD client requires the IP address and the port number of our NBD server exporting your volume.<br/>
In addition, you must specify the block device to export your volume on your server.

This block device must be unused.

For instance: 
```
[root]$nbd-client 10.1.2.242 4320 /dev/nbd1

[root]$fdisk -l -u /dev/nbdXYZ
```

In the above example, `nbd-client 10.1.2.242 4320 /dev/nbd1` connects to the NBD server.<br/>
The output of `fdisk -l -u /dev/nbd1` command shows that the block device `/dev/nbd1` is attached to the server with success.

### Step 2 - Mount and format the volume

In the previous step, the new volume was attached to `/dev/nbd1`.

If the new volume has never been formated, you need to format the volume using `mkfs` before you can mount it.

For instance, the following command creates an `ext4` file system on the volume.

 ```
[root]$mkfs -t ext4 /dev/nbd1
```

Then, to mount the device as /mnt/data, run the following commands.

```
[root]$mkdir -p /mnt/data
[root]$mount /dev/nbd1 /mnt/data
```

Now run the `df -h` command, this command will list all your devices and where they are mounted

```
[root]$df -h

```

### Step 3 - Disconnect a volume

To disconnect a block device you have to follow two steps

First, unmount the filesystem.

Second, disconnect the device from the NBD server.


```
[root]$umount
[root]$nbd-client -d /dev/nbd1
```


