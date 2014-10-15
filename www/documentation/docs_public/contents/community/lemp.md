---
title: Create a LEMP stack Image
template: article.jade
position: 1
---

This page shows you how to create a LEMP stack Image.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)

LEMP stack is a group of open source software to get all tools to run a web application.
The acronym stands for Linux, nginx (pronounced "engine-x") , MySQL, and PHP. 

The image you will create would allow you to create servers with predefined configuration for the LEMP stack.<br />
For instance, you will be able to deploy an infinity of servers serving the LEMP stack in seconds.


There are five steps to create a LEMP Image


- [Create a new server](/community/lemp.html#step-1-create-a-new-server)
- [Install required packages](/community/lemp.html#step-2-install-required-packages)
- [Configure nginx](/community/lemp.html#step-3-configure-nginx)
- [Check PHP and MySQL installation](/community/lemp.html#step-4-check-php-and-mysql-installation)
- [Create the LEMP Image](/community/lemp.html#step-5-create-the-lemp-image)


<iframe width="560" height="315" src="//www.youtube-nocookie.com/embed/RZl-OQpx8mc" frameborder="0" allowfullscreen></iframe>

### Step 1 - Create a new server

Before starting, click the "Create Server" button in the control panel.

![Control Panel](../../images/dashboard.png "Control Panel")

You will land on the server-creation page where you must input basic information for your server:

- The name of your server, for example LEMP
- The tag you want to assign on it (Optional). Tags let you organize your servers, you can assign any tag to each server

![Create server basic information](../../images/create_lemp_server.png "Create server basic information")

After inputting your server basic information, you have to choose a starting Image for your server. Use the <strong>Ubuntu Trusty 14.04</strong> Image to create the LEMP stack Image.

Click the "Create Server" button. This action creates and starts your server. In a few seconds, your server will be ready to use.

### Step 2 - Install required packages

When your server is running, you can log into your server using its public IP address.

In the terminal program and in the shell run the `apt-get update` command to update packages list.

The next step is to install packages required for the LEMP stack. In a terminal execute the following command

```
apt-get install nginx mysql-server php5 php5-cli php5-fpm php5-mysql
```

<strong>Important: During the packages installations, you will be asked to set a root password for MySQL server.</strong>

### Step 3 - Configure nginx

Once the packages installation is achieved, you have to configure nginx to work properly with PHP

In the directory `/etc/nginx/site/available`, create a new file and fill it with the configuration for php. In this guid, I called this file `php_default`

```
server {
  listen   80;


  root /var/www;
  index index.php index.html index.htm;

  server_name example.com;

  location / {
          try_files $uri $uri/ /index.html;
  }

  error_page 404 /404.html;

  error_page 500 502 503 504 /50x.html;
  location = /50x.html {
        root /usr/share/nginx/www;
  }

  # pass the PHP scripts to FastCGI server listening on the php-fpm socket
  location ~ \.php$ {
          try_files $uri =404;
          fastcgi_pass unix:/var/run/php5-fpm.sock;
          fastcgi_index index.php;
          fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
          include fastcgi_params;
        }

}
```

Change to `/etc/nginx/site/enabled` directory. This directory contains the enabled virtual hosts.

Remove the `default` virtual host, enable the `php_default` virtual host and reload nginx configuration.

```
rm /etc/nginx/site-enabled/default
ln -s ../site-available/php_defaut .
service nginx reload
```

### Step 4 - Check PHP and MySQL installation

The LEMP stack is properly installed and configured. You have to check everything is working on.

Connect your MySQL server

```
mysql -u root -p
<you are asked for your password>
```

Create the root web directory and create a file `index.php` displaying the result of `phpinfo()`

```
mkdir /var/www
echo "<?php ehco phpinfo(); ?>" > /var/www/index.php
```

![Php info](../../images/phpinfo.png "Php info")

In your browser, try to access to the public IP address of your server. You should see the php information on the screen as above.

### Step 5 - Create the LEMP Image

You are now ready to create your LEMP Image.

Clean the log files, remove the bash history file and power off the server.

```
find /var/log -type f -delete
history -c
halt
```

In the Control Panel, on the server page set your server to OFF

![Poweroff server](../../images/poweroff_server.png "Poweroff server")

Once your server is powered off, in the volumes list, click the "Snapshot" button on the volume to Snapshot.

![Volume snapshot](../../images/lemp_volume_snapshot.png "Volume snapshot")

In the Control Panel, click "Snapshot" in the compute section.
Click the name of your Snapshot and rename the Snapshot to `LEMP Snapshot`

![LEMP volume snapshot](../../images/lemp_snapshot.png "LEMP volume snapshot")

Select the Snapshot and click the "Create an image from Snapshot" button. Set your image name as `LEMP` and validate.

Create a new server using the `LEMP` Image and power it on. 

![New LEMP server](../../images/new_lemp_server.png "New LEMP server")

Once your server is started, it contains the LEMP stack as you configured it.<br />
You now can deploy an infinity of servers using this Image and serving the LEMP stack in seconds.
