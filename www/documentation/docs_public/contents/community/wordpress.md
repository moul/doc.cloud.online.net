---
title: Create a Wordpress Image
template: article_community.jade
position: 2
---

This page shows you how to create a Wordpress Image.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)
- You have created the [LEMP Image](/community/lemp.html)

WordPress is a popular, free and open source blogging tool and a content management system (CMS) based on PHP and MySQL.

The Image you will create, would allow you to create series of servers with predefined configuration of Wordpress.<br/>
For instance, you will be able to deploy an infinity of servers serving a Wordpress in seconds.

Working with the LEMP Image will significantly save you time and effort as a large base of packages are already installed and configured.

There are five steps to create a Wordpress Image

- [Create a new server using the LEMP image](/community/lemp.html#step-1-create-a-new-server)
- [Install required packages](/community/lemp.html#step-2-install-required-packages)
- [Configure nginx & Wordpress](/community/lemp.html#step-3-configure-nginx)
- [Check Wordpress installation](/community/lemp.html#step-4-check-php-and-mysql-installation)
- [Create the Wordpress Image](/community/lemp.html#step-5-create-the-lemp-image)

### Step 1 - Create a new server using the LEMP image

Before starting, click the "Create Server" button in the control panel.

![Control Panel](../../images/dashboard.png "Control Panel")

You will land on the server-creation page where you must input basic information for your server:

- The name of your server, for example Wordpress
- The tag you want to assign on it (Optional). Tags let you organize your servers, you can assign any tag to each server

![Create server basic information](../../images/create_wordpress_server.png "Create server basic information")

After inputting your server basic information, you have to choose a starting Image for your server.

In this guide, we use the [<strong>LEMP</strong> Image](/community/lemp.html) we created previously to build the Wordpress Image.

<strong>Important: Your Images are presents in the "My images" tab.</strong>

Click the "Create Server" button. This action creates and starts your server. In a few seconds, your server will be ready to use.

### Step 2 - Install required packages

When your server is running, you can log into your server using it's public IP address.

In the terminal program and in the shell run an `apt-get update` to update packages list.

The next step is to install packages required for Wordpress. In a terminal, execute the following command

```
apt-get install php5-gd libssh2-php
```

### Step 3 - Configure nginx & Wordpress

Once packages installation is achieved, you have to configure nginx to work properly with Wordpress

In the directory `/etc/nginx/site/available`, create a new file containing the default virtual host configuration for Wordpress. I called this file `wp_default` in this guide

```
server {
  listen 80 default_server;

  root /var/www;
  index index.php index.html index.htm;

  location / {
          try_files $uri $uri/ /index.php?q=$uri&$args;
  }

  error_page 404 /404.html;

  error_page 500 502 503 504 /50x.html;
  location = /50x.html {
          root /usr/share/nginx/html;
  }

  location ~ \.php$ {
          try_files $uri =404;
          fastcgi_split_path_info ^(.+\.php)(/.+)$;
          fastcgi_pass unix:/var/run/php5-fpm.sock;
          fastcgi_index index.php;
          include fastcgi_params;
  }
}

```

Change to `/etc/nginx/site/enabled` directory. In this directory, are present enabled virtual hosts.

Remove the `php_default` virtual host, enable the `wp_default` virtual host and reload nginx configuration.

```
rm /etc/nginx/site-enabled/default
ln -s ../site-available/wp_defaut .
service nginx reload
```

Wordpress required to have a database to store users, posts, etc. Connecting as root to MySQL, create a database and a database user for Wordpress as following:

```
CREATE DATABASE wordpress;
CREATE USER wpuser@localhost IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON wordpress.* TO wpuser@localhost;
FLUSH PRIVILEGES;
exit
```

Nginx and MySQL are properly configured. Next step is to download the latests version of Wordpress and configure it.

```
cd ~
wget http://wordpress.org/latest.tar.gz
tar xzvf latest.tar.gz
rm -rf /var/www
cp -rf wordpress /var/www
```

In the directory /var/www, copy the file `wp-config-sample.php` in `wp-config.php`


```
cp wp-config-sample.php wp-config.php
```

Edit the following lines of the file `wp-config.php` editing database name, user and password with your settings.

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'wpuser');

/** MySQL database password */
define('DB_PASSWORD', 'password');
```

![WP info](../../images/wpconfig.png "WP info")

In your browser, try to access to the public IP address of your server. You should land on the Wordpress configuration webpage.

### Step 5 - Create the Wordpress Image

You are now ready to create the Wordpress image.

Clean the log files, remove the bash history file and power off the server.

```
find /var/log -type f -delete
history -c
halt
```

In the Control Panel, on the server page set your server to OFF

![Poweroff server](../../images/poweroff_wp_server.png "Poweroff server")

Once your server is powered off, in the volumes list, click the "Snapshot" button on the volume to Snapshot.

![Volume snapshot](../../images/wp_snapshot.png "Volume snapshot")

In the Control Panel, click "Snapshot" in the compute section.
Click the name of your Snapshot and rename the Snapshot to `Wordpress Snapshot`

![WP volume snapshot](../../images/wp_volume_snapshot.png "WP volume snapshot")

Select the Snapshot and click the "Create an image from Snapshot" button. Set your image name as `Wordpress` and validate.

Create a new server using the `Wordpress` Image and power it on. 

![New WP server](../../images/new_wp_server.png "New WP server")

Once your server is started, it contains a Wordpress as we configured it.<br />
You now can deploy an infinity of servers using this Image and serving Wordpress in seconds.
