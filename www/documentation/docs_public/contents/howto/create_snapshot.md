---
title: Backup your data with snapshots
template: article.jade
position: 2
---

This page shows you how to backup your servers and their data.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/account/ssh_keys.html)
- You have a running [server](/howto/create_instance.html)

A snapshot is a full-volume copy stored in our secure data centers.<br/>
Snapshots are perfect if you want to recover a server from a previous state. 

Potential uses:

- Recover volume data
- Create a copy from a volume

There are three steps to create a snapshot:

- [Powered off your server](/howto/create_snapshot.html#step-1-power-off-your-server)
- [Select the volume to snapshot](/howto/create_snapshot.html#step-2-select-the-volume-to-save)
- [Verify the snapshot creation](/howto/create_snapshot.html#step-3-verify-the-snapshot-creation)

There are three steps to create a new server from a snapshot:

- [Name your server](/howto/create_snapshot.html#step-1-name-you-server)
- [Choose your snapshot as image](/howto/create_snapshot.html#step-2-choose-your-snapshot-as-image)
- [Create your server](/howto/create_snapshot.html#step-3-create-your-server)

## Create a snapshot

In the Control Panel, click "Servers" in the compute section.

### Step 1 - Power off your server

Focus on the server with the volume you want to snapshot and click the "Off" button.

![Create snapshot](../../images/create_snapshot.png "Create snapshot")

### Step 2 - Select the volume to save

Once your server is powered off, in the volumes list, click the "Snapshot" button on the volume to snapshot.

![Volume snapshot](../../images/volume_snapshot.png "Volume snapshot")

### Step 3 - Verify the snapshot creation

In the Compute section of the console click "Volumes", your new snapshot should be present on snapshots list.

![Volumes list snapshot](../../images/volumes_list_snapshot.png "Volumes list snapshot")

## Restore a volume from a snapshot

In the previous step, we create a snapshot.
We will create a new server based on the snapshot we take previously.

In the Control Panel, click the "Create Server" button.

###  Step 1 - Name you server

You will land on the server-creation page where you must input basic information for your server.

### Step 2 - Choose your snapshot as image

In the image section, click the "Snapshots" tab. Select the snapshot you take previously from the list below.

### Step 3 - Create your server

Click the "Create Server" button. This action starts your server. In a few seconds, your server will be ready to use.

All data stored stored when you create your snapshot will be present on this new server.