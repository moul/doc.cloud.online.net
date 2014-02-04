---
title: 3S SSV Scaleway Scalable Volumes/Storage
template: article.jade
---

#### Intro

You can add extra storage on a running instance by adding Scaleway volumes to an existing server.
A volume is at most attach to one instance.

This guide is about volumes managment

#### Sign in

In a first time go to the [Scaleway dashboard](xxx) and log in with your email and password.

Then, click on the “Volumes” button on the left sidebar

#### Creating new volume

##### Step 1

Choose if you wish to "Create new volume" or "Create from existing volume".

- Create new volume

Create a volume from scratch

- Create from existing volume

Create from a snapshot volume [See volume snapshot documentation](xxxx)

#### Step 2 - Create new volume

First, you have to name your volume, a volume name as the following specifications: It can be from 1 to 64 characters without symbols.

Choose the size of your volume, the volume size must be at least 1Gb and can't exceed 1Tb

Then select the volume type you need :

- Scalable distributed storage
99.999% availability and 99.999% reliability over a year, sustain the loss of data in 200+ data centers. recommended for high redundancy.

- Ultra low latency
SSD disk to deliver faster disk I/O performance, it's perfect if you need heavy read/write

#### Attach a volume

Since your volume is created, you will need to attach it to a specific instance.

From the volumes list, select the volume to attach and click the button "Attach", a popup appear asking on which instance you want to attach. Once select, submit your choice.

#### Detach a volume

If you want to detach a volume used by an instance, turn off the specific instance and go to the Volumes menu.

On the list, select the volume you want to detach, attached volumes have a server name not blank in the `Server` column.

Then select the volume to detach and click the "Detach" button.

#### Delete

A volume is unused and you don't still need it ?

From the volumes list, select the volume to delete and click "Delete selected" button.







