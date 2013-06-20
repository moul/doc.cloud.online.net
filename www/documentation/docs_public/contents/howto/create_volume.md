---
title: Attach and detach a volume
template: article.jade
position: 2
---

This page shows you how to attach and detach additional volumes to an existing server.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)
- You have a [server](/howto/create_instance.html)

Each server that you create can have at most fifteen additional volumes. <br/>
You can select the type of disk to host your volumes from two technologies:

- LSSD (Local solid state drive), to deliver fast disk I/O (Local solid state drive)
- LHDD (Local spinning disk), use for moderate read/write access.

There are two steps to attach a volume to an existing server

- [Create a new volume](/howto/create_volume.html#step-1-create-a-new-volume)
- [Attach an existing volume to your instance](/howto/create_volume.html#step-2-attach-an-existing-volume-to-your-instance)

<strong>Important</strong>: Server must be powered off to attach or detach a volume.

## Attach a volume to an existing server

In the Control Panel, click "Volumes" in the compute section.

### Step 1 - Create a new volume

Click the "Create Volume" button.<br/>
You will land on the volume-creation page where you must input basic information for your volume:

- The name of your volume
- The volume type - LSSD (Local solid state drive) or LHDD (Local spinning disk)
- The size in Go

![Create new volume](../../images/create_new_volume.png "Create new volume")

### Step 2 - Attach an existing volume to your instance

In the servers page, click on the server you want to attach a volume to.

![Create new volume](../../images/attach_volume.png "Create new volume")

On the server detail page click "Attach an existing volume" and select the volume to attach in the list.

<strong>Important</strong>: To detach the volume, click the Detach button.