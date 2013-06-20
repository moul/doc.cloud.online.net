---
title: Server boot process
template: article.jade
position: 2
---

This page explains you the boot process of a server.

Thereafter are described the different state of a server boot

While booting your server will go through five different steps:

- <strong>Allocating node</strong> - Our system received your request
- <strong>Provisioning node</strong> - Our system locate a node to start your server and fetch local disks 
- <strong>Booting kernel</strong> - Self explaining
- <strong>Kernel booted</strong> - Initramfs, mount your root volume
- <strong>Booted</strong> - You server is ready and you can connect to it

When you start a server, you can follow the current state of the boot

![Boot process](../../images/boot_process.png "Boot process")