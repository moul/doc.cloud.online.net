---
title: Boot a server in rescue
template: article.jade
position: 10
---

This page shows you how to boot a C1 server in rescue. The rescue mode allows you to debug your server.

> <strong>Requirements</strong>
- You have an account and are logged into [https://cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](https://doc.cloud.online.net/howto/ssh_keys.html)
- You have a [server](https://doc.cloud.online.net/howto/create_instance.html)

## The rescue bootscript

A rescue bootscript is available to help you debugging your server.
The rescue bootscript creates a ramdisk with the content of a downloaded rootfs. You will have access to all your disks and will be able to perform debug/rescue actions.

<strong>important:</strong> If you attach the rescue bootscript while your server is running, you will have to reboot the server to apply changes.

In the Control Panel, click "Servers" in the left panel.

![Servers list](../../images/servers_list.png "Servers list")

Select the server you want to start in rescue mode and click on the "Off" button. In the server details, display advanced options.

The list of available bootscripts appears. Select the rescue bootscript. In my case, I selected the bootscript "Rescue - Linux 3.17 96-std". Validate.

![Server bootscript](../../images/server_bootscript.png "Server bootscript")

Power on your server. In a few seconds, your server will be running in rescue mode.
Your server will be running and you will have access to all your disks and will be able to perform debug/rescue actions.
