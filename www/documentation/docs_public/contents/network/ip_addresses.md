---
title: IP Addresses
template: article.jade
position: 1
---

This page shows you how to create and attach, reassociate and delete a reserved IP to a server.

Requirements

- You have a labs.online.net account
- You have Setting up your ssh key
- You need to have at least a running server

An image is a kind of "Box" that includes one or more volumes containing the operating system (e.g., Linux) and any additional software required to deliver a service or a portion of it.<br/>

When you create a server, we assign it a dynamic IP address at launch, if you power off or reboot the server IP can change.<br/>
To avoid this thing to happen, you can use reserved IP. Reserved IP are persistent and are mapped to of your servers.

There are 3 step to allocate a reserved ip to server 

- Create and attach a reserved IP
- Reassociate a reserved IP to another server
- Delete a reserved IP

From the dashboard click "Network" section of your console. The list of Ips mapped appear if there are.

### Step 1 - Create and attach a reserved IP

  1. Click on Create new ip 
  2. Select the instance you want to attach the IP address

  ![Create new IP](../../images/create_new_ip.png "Create new IP")

### Step 2 - Reassociate a reserved IP to another server

  1. Focus on the ip you want to reassociate
  2. In the association dialog box, select the new instance to associate the IP

  ![Reassociate ip](../../images/reassociate_ip.png "Reassociate ip")

### Step 3 - Delete a reserved IP

  1. Select the ip wou want to delete
  2. Click on delete button

  ![Delete ip](../../images/delete_ip.png "Delete ip")
