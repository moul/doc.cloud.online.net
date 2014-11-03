---
title: Boot a server with a specific kernel
template: article.jade
position: 2
---

This page shows you how to boot a C1 server with a specific bootscript. Bootscripts allow you to start a server with a specific Kernel version.

> <strong>Requirements</strong>
- You have an account and are logged into [https://cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](https://doc.cloud.online.net/howto/ssh_keys.html)
- You have generated your [API Token](https://doc.cloud.online.net/howto/credentials.html)
- You have a [server](https://doc.cloud.online.net/howto/create_instance.html)

A bootscript is composed of three elements:

- The kernel
- The initrd - An archive containing the scripts needed to fetch the missing kernel modules and dynamically mount your NBD root volume, fully loaded in RAM before loading your volumes
- The cmdline - Passed to the kernel at startup. Available for the initrd scripts and available from the server with the following command `cat /proc/cmdline`

This guid show you how to boot your C1 server with a specific bootscript

- [Change servers bootscript](/advanced/bootscripts.html#change-servers-bootscript)
- [The rescue bootscript](/advanced/bootscripts.html#the-rescue-bootscript)

<strong>important:</strong> If you attach a bootscript while your server is running, you will have to reboot the server to apply changes.

## Change servers bootscript

In the Control Panel, click "Servers" in the left panel.

![Servers list](../../images/servers_list.png "Servers list")


Select the server you want to change the bootscript and click the "Off" button. In the server details, display advanced options.

The list of available bootscripts appears. Then select the bootscript you want to start your server with and validate.

![Server bootscript](../../images/server_bootscript.png "Server bootscript")


Power on your server. In few seconds, your server will be running with the new bootscript.
Connect your server and run `uname -a`. In my case I changed the kernel version to `3.17.0-63`. 

```
root@c1-X-Y-Z-T:~#uname -a
Linux c1-X-Y-Z-T 3.17.0-63 #8 SMP Mon Oct 13 21:39:09 CEST 2014 armv7l armv7l armv7l GNU/Linux
```

## The rescue bootscript

A rescue bootscript is available to help you debugging your server.
The rescue bootscript create a ramdisk with the contents of a downloaded rootfs. You will have access to all your disks and will be able to perform debug/rescue actions.