---
title: Backup your data with snapshots
template: article.jade
position: 2
---

This page shows you how to backup your servers and their data.

Requirements

- You have a labs.online.net account
- You have Setting up your ssh key
- You need to have at least a running server

A snapshot is a full-volume copy stored in our secure data centers.

There are 4 steps to create a snapshot of a volume

- Power off your server
- Select the volume to snapshot
- Verify the snapshot creation

## Create a snapshot

### Step 1 - Power off your server

From the dashboard click "Servers" in the Compute section of your console.

Focus on the server with the volume you want to snapshot and click the "Off" button

![Create snapshot](../../images/create_snapshot.png "Create snapshot")

### Step 2 - Select the volume to save

Once your server is powered off, in the volumes list, click the "Snapshot" button on the volume to snapshot

![Volume snapshot](../../images/volume_snapshot.png "Volume snapshot")

### Step 3 - Verify the snapshot creation

In the Compute section of the console click "Volumes" and your new snapshot should be present on snapshots list

![Volumes list snapshot](../../images/volumes_list_snapshot.png "Volumes list snapshot")

## Restore a volume from a snapshot

Coming soon