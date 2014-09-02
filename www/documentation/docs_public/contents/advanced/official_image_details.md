---
title: Official image content
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

### Included services

All the following services are present by default on all servers

#### NTP Server

Network Time Protocol (NTP) is configured by default on every server.
The system time is synchronized with our NTP servers and set to the UTC timezone.

You can execute the ntpq -p command on your server to see the details list of peers known to the NTP server.

```
ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 10.1.31.38      172.16.2.6       4 u   15   64    7    0.311    2.796   2.392
 golem.canonical 192.93.2.20      2 u   13   64    7   15.250    6.745   2.095
```

For more information about NTP, go to [http://www.ntp.org/](http://www.ntp.org/).

#### DNS Server

Every server are configured to use our DNS servers to resolve domain name.

#### Mirror

Every Ubuntu server use the following mirror `http://mirror.cloud.online.net` for fast updates as is it close from your servers.


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



