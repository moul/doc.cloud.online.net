---
title: Launch your first instance
template: article.jade
---

##Intro

A Scaleway instance is physical server, each instance that you create is a physical instance dedicated for your personnal use.
It's easy to use, the entire process take only a couple of minutes!

This guide gonna show you how to create and access your new server.

##Step 1 - Sign in

In a first time go to the [Scaleway dashboard](xxx) and log in with your email and password.

Once logged, click on the “Create Server” button at the top right of the sidebar

##Step 2 - Choose an organization

Empty

##Step 3 - Name & Tags your instance

First, you have to name your server, an instance name as the following specifications: It can be from 1 to 64 characters without symbols.

To help you manage your instances, and other resources, you can assign your own metadata to each resource in the form of tags. A tags as is a string with the following restrictions :

- Maximum number of tags per resource: 10
- Maximum length: 255 Unicode characters

Tag are case sensitive.

##Step 4 - Choose your image

To create your server, you have 3 options, use:

- Scaleway images

They are standard OS Images, we propose today some linux operating systems, such as Ubuntu, Fedora or Debian... What else ? (list is update permanently).

- Market place

This section provide you custom images build by the community, they often run with pre-installed or configured services that will allow save you time.

- Snapshots

It's the list of your instance snapshot, it allow you to start a new instance form a previous one. It could be really usefull for scaling.

##Step 5 - Add storage

You can add some volume to your instance, it can be an existing volume or new one.
An existing volume is a disk snapshot that you take previously

Volume size is limit to 1Tb and there is no limit on the amount of volumes you can attach to your server.

Your volume can be of type :

- Scalable distributed storage
99.999% availability and 99.999% reliability over a year, sustain the loss of data in 200+ data centers. recommended for high redundancy.

- Ultra low latency
SSD disk to deliver faster disk I/O performance, it's perfect if you need heavy read/write

##Step 6 - Create your server

Well, it's now time to start your instance, just click the "Create server" button. In few seconds your instance will be ready to use.
If you have not configured your ssh key, you will receive an email with the root password.

##Step 7 - Connect your instance

###Login from OSX and Linux

####1 - Launch a terminal

On a Mac or Linux computer, open your terminal program and in the shell just type the following command :

```sh
ssh root@your_instance_ip
```

####2 - Allow the connection to the host

Answer "yes" when the prompt asks if you want to connect to the host.

####3 - Done

You are now ask to type your root password (root password was emailed previously) and press enter.

Well done, you are now connected to your instance!

###Login from Windows

On windows, you will need a small apllication named PuTTy, and ssh client. You can download putty [here](xxx)
Once PuTTY is downloaded and installed, just start the program.

Fill in the "Hostname" with your instance IP address and click connect. You are now connected to your instance from windows!


