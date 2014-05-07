---
title: Create your first instance
template: article.jade
position: 1
---

Each instance that you create is a physical server dedicated for your personal use.<br/>
After you've launched your instance, you can connect and use it.

The following procedure is intended to help you to launch an instance in seconds.

### Step 1 - Name & Tags your instance

From, the dashboard, click the Create Server button.

![Create server](../../images/dashboard.png "Dashboard")

You land on the instance creation section and have to set basic informations for your server: The name of your instance, the tags you want to assign on it.

Tags help you to manage your instances, and other resources, you can assign your own tags to each resource.

![Create instance basic informations](../../images/instance_basic_informations.png "Instance-basic-informations")

### Step 2 - Choose your image

Since you have set instance basic informations, you have to choose which image your instance will use. You can choose from

- Images: They are standard OS Images, we propose today some Linux operating systems, such as Ubuntu, Fedora or Debian... What else ? (list is update permanently).

- Market place: This section provide you custom images build by the community, they often run with pre-installed or configured services that will allow save you time.

- Snapshots: It's the list of your instance snapshots, it allow you to start a new instance form a previous one. 

![Create instance image](../../images/instance_image.png "Instance-image")

### Step 3 - Add storage

You have to add at least one volume to your instance, it can be an existing volume or new one.<br/>
An existing volume is a [snapshot](/servers/volumes/snapshot.html) that you take previously.

Volume size is limit to 1Tb and there is no limit on the amount of volumes you can attach to your server.

Your volume can be of type :

- Low latency Local storage on spinning disk, use for moderate read/write access

- Ultra low latency SSD disk to deliver faster disk I/O performance, it's perfect if you need heavy read/write

![Create instance volumes](../../images/instance_volume.png "Instance-volume")

### Step 4 - Create your server

Well, it's now time to start your instance, just click the "Create server" button. In few seconds your instance will be ready to use.

If you have not configured your ssh key, you will receive an email with the root password.

### Step 6 - Connect your instance

#### Login from OSX and Linux

- 1 - Launch a terminal

On a Mac or Linux computer, open your terminal program and in the shell just type the following command :

```sh
ssh root@your_instance_ip
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

Well done, you are now connected to your instance!

#### Login from Windows

On windows, you will need a small apllication named PuTTy, and ssh client. You can download putty [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
Once PuTTY is downloaded and installed, just start the program.

Fill in the "Hostname" with your instance IP address and click connect. You are now connected to your instance from windows!

