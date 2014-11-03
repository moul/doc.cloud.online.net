---
title: Pydio with Cloud Storage
template: article.jade
position: 2
---

This page shows you how to spawn a Pydio application with Cloud Storage.

> <strong>Requirements</strong>
>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)
- You have generate your [API Token](/howto/credentials.html)

Pydio is an open source software solution for file sharing and synchronization. With intuitive user interfaces (web / mobile / desktop).

The Pydio application will store files in our Cloud Storage thereby you have an highly available and unilimited storage.

There are two steps to deploy the Pydio application

- [Name & tag your server](/applications/pydio.html#step-1-name-tag-your-server)
- [Choose the Pydio application](/applications/pydio.html#step-2-choose-the-pydio-application)
- [Start the server](/applications/pydio.html#step-3-start-your-server)
- [Access your server URL](/applications/pydio.html#step-4-access-your-server-url)
- [Configure Pydio](/applications/pydio.html#step-5-configure-pydio)
- [Login and start using Pydio](/applications/pydio.html#step-6-login-and-start-using-pydio)
- [Configure Pydio with Cloud Storage](/applications/pydio.html#step-7-configure-pydio-with-cloud-storage)

Before starting, click the "Create Server" button in the control panel.

![Control Panel](../../images/dashboard.png "Control Panel")

### Step 1 - Name & tag your server

You will land on the server-creation page where you must input basic information for your server:

- The name of your server
- The tag you want to assign to it (Optional). Tags let you organize your servers, you can assign any tag to each server.

![Create server basic information](../../images/server_basic_information.png "Create server basic information")

### Step 2 - Choose the Pydio application

After inputting your server basic information, you have to choose a starting application for your server.

On the Applications tab, select Pydio. The server will be created with a ready to use Pydio.

![Create server image](../../images/server_image.png "Create server image")

### Step 3 - Start your server

Click the "Create Server" button. This action starts your server.
In a few seconds, the Pydio application will be ready to use.

### Step 4 - Access your server URL

When your server is running, you can see the server's IP address in the server list on the control panel. Copy this IP address and paste it in your favorite browser.

### Step 5 - Configure Pydio

You land on the Pydio diagnostic page. All checks are "OK" except the SSL encryption which is disabled.

![Pydio diag](../../images/pydio_diag.png "Pydio diag")

Click on the "click here to continue to Pydio." link to continue the installation.

You are asked to fill-in:

#### The admin access

![Pydio admin](../../images/pydio_admin.png "Pydio admin")


#### The global options

![Pydio options](../../images/pydio_global_options.png "Pydio options")

#### The configuration storage

Pydio uses a MySQL database as configuration storage. To retrieve the database credentials, connect your server using a terminal `ssh root@<your_server_ip>`.
If you are not familiar with ssh, you can read the following documentation: [Log-into your server](/howto/create_instance.html#log-into-your-server)

In the root directory of your server, execute the following command `cat .my.cnf`. It will display your database credential (user and password).

```
root@c1-X-Y-Z-T:~#cat .my.cnf
[client]
user = root
password = ootaitevohxeizasinaeguasofaiwiuzuekohbicut
```

In the Pydio setup wizard, fill-in the database user and password you retrieve from the `.my.cnf` file and click the "Install Pydio Now" button
 
![Pydio storage](../../images/pydio_storage.png "Pydio storage")

### Step 6 - Login and start using Pydio

Pydio is now installed and ready to use. Input the username and password you set during the configuration and login

![Pydio home](../../images/pydio_home.png "Pydio home")

### Step 7 - Configure Pydio with Cloud Storage

Before starting, click the "Storage" button in the Online Labs control panel.
You will land on the Storage page.

The first thing to do is to create a new bucket for Pydio to store files inside.<br/>
A bucket name must contain only alphanumeric and lowercase characters

Then, click on the "S3 Credentials" button.<br/>
The credentials required to access Cloud Storage are displayed:

- `host_base`  base url to access Cloud Storage service
- `access_key` the access key required for Cloud Storage 
- `secret_key` the API Token you generated previously.

![S3 Crendentials](../images/s3.png "S3-credentials")


On the left panel of Pydio settings, click Workspaces and New Workspace. Select "S3 Amazon Web Service" as driver and fill-in with your S3 credential.

- KEY: your `access key`
- SECRET KEY: your `secret_key`
- STORAGE URL: `https://fr-1.storage.online.net`
- BUCKET: The name of the bucket you created

When you have filled all inputs, submit.

![Pydio settings](../images/pydio_settings.png "Pydio settings")

You now have a new workspace using Cloud Storage that allow you to have an highly available and unilimited storage.


![Pydio cs](../images/pydio_cs.png "Pydio cs")



