---
title: Instance operations
template: article.jade
---

#### Intro

A Scaleway instance is physical server, each instance that you create is totally  dedicated for your personnal use.

This guid is about instance operations such as create, edit, delete.

#### Sign in

In a first time go to the [Scaleway dashboard](xxx) and log in with your email and password.

Once logged, click on the “Create Server” button at the top left of the sidebar


### Instance creation

Once logged, click on the “Create Server” button at the top left of the sidebar

#### Step 1 - Choose an organization

Empty

#### Step 2 - Name & Tags your instance

First, you have to name your server, an instance name as the following specifications: It can be from 1 to 64 characters without symbols.

To help you to manage your instances, and other resources, you can assign your own metadata to each resource in the form of tags. A tags as is a string with the following restrictions :

- Maximum number of tags per resource: 10
- Maximum length: 255 Unicode characters

Tags are case sensitive.

#### Step 4 - Choose your image

To create your server, you have 3 options, use:

- Scaleway images

They are standard OS Images, we propose today some linux operating systems, such as Ubuntu, Fedora or Debian... What else ? (list is update permanently).

- Market place

This section provide you custom images build by the community, they often run with pre-installed or configured services that will allow save you time.

- Snapshots

It's the list of your instance snapshot, it allow you to start a new instance form a previous one. It could be really usefull for scaling.

#### Step 5 - Add storage

You can add some volume to your instance, it can be an existing volume or new one.
An existing volume is a disk snapshot that you take previously

Volume size is limit to 1Tb and there is no limit on the amount of volumes you can attach to your server.

Your volume can be of type :

- Scalable distributed storage
99.999% availability and 99.999% reliability over a year, sustain the loss of data in 200+ data centers. recommended for high redundancy.

- Ultra low latency
SSD disk to deliver faster disk I/O performance, it's perfect if you need heavy read/write

- Choose security group

A security group acts as a firewall that controls the traffic for one or more instances.

#### Step 6 - Create your server

Well, it's now time to start your instance, just click the "Create server" button. In few seconds your instance will be ready to use.
If you have not configured your ssh key, you will receive an email with the root password.


### Edit instance

At any time you can edit your instance and update it name, tags, etc.

#### Step 1- Choose the instance to edit

From the Servers link in the menu you will land on the instances list page. Then, select the server you want to edit.

#### Step 2- Update instance

At the moment you can modify your instance name and tags set.

Instance name as the following specifications: It can be from 1 to 64 characters without symbols.

A tags as is a string with the following restrictions :

- Maximum number of tags per resource: 10
- Maximum length: 255 Unicode characters

Tags are case sensitive.

### Delete instance

To delete an instance just go to your instances list.

#### Step 1- Instance deleting

Choose in the servers list the instance you want to terminate and click delete on the instances menu. Then, confirm the instance removing.

Your instance will be kill instantly and billing will be interupt.
