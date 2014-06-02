---
title: IP Addresses
template: article.jade
position: 1
---

This page shows you how to create, attach, re-associate and delete a reserved IP address to a server.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)
- You have a running [server](/howto/create_instance.html)

When you create and powered on server, the server IP address is assign dynamicly. If you powered off or reboot the server IP address change.<br/>
To avoid IP address change to happen, you can use reserved IP. Reserved IP are persistent and are mapped to a specific server.

N.B: If you power-off / power-on a server which you have assigned a reserved ip, you will have to remap it.

Theis procedure is composed of three steps:

- Create and attach a reserved IP address
- Re-associate a reserved IP address to another server
- Delete a reserved IP address

In the Control Panel, click "Network" in the compute section.

### Step 1 - Create and attach a reserved IP address

Click on "Create New Ip"

![Create new IP](../../images/create_new_ip.png "Create new IP")

Select the instance you want to attach the IP address

### Step 2 - Re-associate a reserved IP address to another server

Focus on the ip you want to reassociate

![Reassociate ip](../../images/reassociate_ip.png "Reassociate ip")

In the "Association" dialog box, select the new instance to associate the IP address

### Step 3 - Delete a reserved IP address

Select the ip wou want to delete

![Delete ip](../../images/delete_ip.png "Delete ip")

Click on "Delete" button
