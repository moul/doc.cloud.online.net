---
title: Server boot process
template: article.jade
position: 2
---

This page explains you the boot process of a server.

Thereafter are described the different states of a server boot.

While booting, your server will go through five different steps:

- <strong>Allocating node</strong> - Your start request has been received and our control plane is trying to locate an available node
- <strong>Provisioning node</strong> - Our control plane is launching the tasks to start your server 
- <strong>Booting kernel</strong> - The kernel is booting, local volumes are downloaded in parallel
- <strong>Kernel booted</strong> - The kernel is booted and the initramfs is trying to mount your root volume
- <strong>Booted</strong> - You server is ready and you can connect to it

When you start a server, you can follow the current state of the boot

![Boot process](../../images/boot_process.png "Boot process")