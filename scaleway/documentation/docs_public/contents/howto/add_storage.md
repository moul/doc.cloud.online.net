---
title: Add extra storage
template: article.jade
---

##Intro

It could happen that you need top add more storage to your existing servers.
Scaleway allow you to attach more storage volume to an existing instance.

This guide gonna show you how to create and attach additional volume to an existing instance

##Step 1

From the console, on the right side panel go to storage section

You will arrive on a page were you are ask to create new volumes if you still don't have create one, or the list of existing volumes will be shown.

##Step 2

To create your volume, simply click on "Create new volume" button.
Then you will be ask  to choose if you wish to "Create new volume" or "Create from existing volume".

##Step 3 - Create new volume

First, you have to name your volume, a volume name as the following specifications: It can be from 1 to 64 characters without symbols.

Choose the size of your volume, the volume size must be at least 1Gb and can't exceed 1Tb

Then select the volume type you need :

- Scalable distributed storage
99.999% availability and 99.999% reliability over a year, sustain the loss of data in 200+ data centers. recommended for high redundancy.

- Ultra low latency
SSD disk to deliver faster disk I/O performance, it's perfect if you need heavy read/write

##Step 4 - Create from existing volume

The process is the that explain in step3, the only difference is that you don't have to choose a size for the volume but a snapshot form a previous one.

Once it's ok, just create it!

##Step 5

Well, you are now on your volume details page, just click "More" button, attach.

A popin show you the list of servers you own, select the instance you attach the volume and it's done!






