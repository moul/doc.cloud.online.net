---
title: IP Addresses
template: article.jade
position: 11
---

This page shows you how to create, attach, and delete a reserved IP address to a server.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)
- You have a running [server](/howto/create_instance.html)

A freshly-created server has a dynamic IP address.<br/>
If you poweroff or reboot the server IP address changes.<br/>

You can reserve IP addresses in the Control Panel. You then have to configure which server gets which reserved IP.

### Create and attach a reserved IP address

In the Control Panel, click "Network" in the compute section.

Click on "Create New Ip"

![Create new IP](../../images/create_new_ip.png "Create new IP")

Select the instance you want to attach the IP address to

### Release a reserved IP address
In the Control Panel, click "Network" in the compute section.

Select the IP you want to delete

![Delete IP](../../images/delete_ip.png "Delete ip")

Click on the "Delete" button
