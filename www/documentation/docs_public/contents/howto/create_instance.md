---
title: Provisioning your first server
template: article.jade
position: 1
---

This page shows you how to launch and connect to your servers.

Each server that you create is a physical server dedicated for your personal use.<br/>
After you've launched your server, you can connect and use it.

There are 4 steps to provision your first server

- Name & Tags your server
- Choose your image
- Add storage
- Create & Start server

## Server creation

From the dashboard, click the Create Server button.

![Dashboard](../../images/dashboard.png "Dashboard")

### Step 1 - Name & Tags your server

You'll be prompted to the server creation section and have to set basic informations for your server

- The name of your server
- The tags (Optional) you want to assign on it

Tags help you to organize your servers, you can assign your own tags to each server.

![Create server basic informations](../../images/server_basic_information.png "Create server basic informations")

### Step 2 - Choose your image

An image is a kind of "Box" that includes an operating system (e.g., Linux) and any additional software required to deliver a service or a portion of it.<br/>

Since you have set server basic informations, you have to choose which image your server will use.
You can choose from three sources

- Marketplace: They are standard OS Images, we propose today some Linux operating systems, such as Ubuntu, Fedora or Debian... What else ? (list is update permanently).

- My images: It's the list of images that you create from snapshot previously, it allow you to start a new server from a previous one.

- Snapshots: Like images, it allows you to start a new server form a volume previously snapshoted. 

![Create server image](../../images/server_image.png "Create server image")

### Step 3 - Add storage

Additionnaly to the image you selected, you can add extra storage to your server, it can be an existing volume or new one.<br/>

Volume size is limited to 1Tb and there is no limit on the amount of volumes you can attach to your server.

Your volume can be of type :

- LHDD, spinning disk, use for moderate read/write access

- LSSD disk to deliver faster disk I/O performance, it's perfect if you need heavy read/write

![Create server volumes](../../images/server_volume.png "Create server volumes")

### Step 4 - Create & Start your server

The "Create server" button will create and start your server. In few seconds your server will be ready to use.

If you have not configured your ssh key, you will receive an email with the root password.

## Log into your server

### For OSX and Linux

- 1 - Launch a terminal

On a Mac or Linux computer, open your terminal program and in the shell just type the following command :

```
ssh root@your_server_ip
```

- 2 - Allow the connection to the host

Answer "yes" when the prompt asks if you want to connect to the host.

- 3 - Done

You are now ask to type your root password (root password was emailed previously) and press enter.

```sh
The authenticity of host 'myhost.ext (54.195.242.119)' can't be established.
RSA key fingerprint is 4f:ba:65:cf:14:64:a7:1e:b6:07:7c:00:71:95:21:fa.
Are you sure you want to continue connecting (yes/no)?
```

Well done, you are now connected to your server!

### For Windows

On windows, you will need a small apllication named PuTTy, and ssh client. You can download putty [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
Once PuTTY is downloaded and installed, just start the program.

Fill in the "Hostname" with your server IP address and click connect. You are now connected to your server from windows!

