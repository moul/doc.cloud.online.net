---
title: 3S SSV Snapshot
template: article.jade
---

#### Intro

Snapshots are extremly usefull in production like in development environment.
A snapshot is a copy of a volume.

This documentation will show you how to use Snapshot to backup specifics volumes, recover it, and delete it.

#### Sign in

In a first time go to the [console](https://console.cloud.online.net) and log in with your email and password.

#### Create a new snapshot

First power-off the instance on which you want to create a volume snapshot.

You can do it from the console or form the command line using this command: `sudo halt`

Then, click on "Volumes" from the left-hand menu in the onsole, the list of volumes will appear.
Select the volumes you want to snapshot on the list and click the "Snapshot" button.

A popup will appear asking you for the snapshot name, description, tags and if you want to start the server once the snapshot is achieve.

![Console](../imgs/howto/img_tmp_dashboard.png "Temporaire")

In few minutess your snapshot will be ready and will appear in the snapshots section.

#### Restore a snapshot

Restore a volume snapshot is fast and simple, from your volumes snapshot list select the volumes to restore.

Next, click the "Restore" snapshot button, give it a name, description and tags.

The new volume will appear in the volumes list, then you just have to attach it to the instance you need.

#### Delete a snapshot

To delete a snapshot, from the snapshots list select the snapshot to delete.
Once selected, click the "Remove" button.

Your snapshot is delete instantly.
