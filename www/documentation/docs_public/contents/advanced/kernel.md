---
title: Official Linux kernel
template: article.jade
position: 10
---

This page give you more information on how our kernel works.

For now, you can only boot with our official kernel, even if you build a new one, the kernel is not loaded from your volume.

### .config

You can retrive the .config content running the following command:

```
zcat /proc/config.gz
```

The project is also available on [github](https://github.com/online-labs/kernel-config/)

### cmdline

The cmdline passed to the kernel is available at /proc/cmdline

### kernel modules

Kernel modules are downloaded at the server boot.<br />
If you want to refresh the kernel modules on your server follow this process:

```
root@c1-X-Y-Z-T:~# rm -rf /lib/modules/$(uname -r)
root@c1-X-Y-Z-T:~# oc-sync-kernel-modules
```

### Customisations and next features

You can follow the kernel related information progress [here](https://community.cloud.online.net/t/official-linux-kernel-new-modules-optimizations-hacks/226)

We invite you to contribute on our dedicated [topic](https://community.cloud.online.net/t/official-linux-kernel-new-modules-optimizations-hacks/226) and give us information about your needs (the best would be .config lines)

