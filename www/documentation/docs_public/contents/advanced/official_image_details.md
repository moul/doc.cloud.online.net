---
title: What is the official image composed of?
template: article.jade
position: 1
---

This page describes the content of the official image Ubuntu Trusty (14.04)

When you create a new server for the first time you have to select an official image.<br/>
This image has the following characteristics.

### Pre-installed packages

The official image comes with extra packages:
```
ssh, rsyslog, nano, less, man-db, net-tools, iputils-ping, whiptail, wget, nbd-client, xnbd-client, isc-dhcp-client, curl, sudo, iptables, ntp, ntpdate, vim, ca-certificates
```

These packages are official packages without patches.

### Additional upstart jobs

The following scripts and configurations ensure that your server works properly on our infrastructure.

- `/etc/init/ttyS0.conf` Maintains a getty on ttyS0
- `/etc/init/nbd-root-preserve-client.conf` Preserves the NBD client process on shutdown
- `/etc/init/nbd-root-disconnect.conf` Gracefully umount and disconnect root volume
- `/etc/init/nbd-add-extra-volumes.conf` Connects additional volumes to NBD server
- `/etc/init/ssh-keys.conf` Fetches ssh-keys associated with your account in `/root/.authorized_keys`
- `/etc/init/sync-kernel-modules.conf` Synchronizes kernel modules

### Additional files

Often you will want to automate your server configuration based on data unavailable before start.

For instance, if you use server tags to configure your monitoring, you can retrieve these data using the following executable.

- `/usr/local/bin/oc-metadata` Executable which retrieves server metadata (TEXT)
- `/usr/local/bin/oc-metadata-json` Executable which retrieves server metadata (JSON)
- `/usr/sbin/oc-sync-kernel-module` Executable which synchronizes kernel modules

In addition, this script is required by `/nbd-root-disconnect.conf` to disconnect root volume gracefully.

- `/usr/sbin/nbd-disconnect-root`
