---
title: Create your own image
template: article.jade
position: 5
---

This page shows you how to create an image from a server.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)
- You have a running [server](/howto/create_instance.html)
- You have installed packages and made the configuration you need on your server
- You have created a [snapshot](/howto/create_instance.html) of the volume you want to be an image

Images allow you to create series of servers with predefined configuration.<br/>
For instance, you can prepare to scale your serving capacity with a frontend image for an Apache server.

Potential uses

- Automate Server Builds
- Create a Software Testing Environment

There are three steps to create an Image:

- Powered off your server
- Create an Image
- Verify Image creation

There are three steps to create a server from an Image

- [Create an Image from a volume snapshot](/howto/create_image.html#step-1-create-an-image-from-a-volume-snapshot)
- [Image creation](/howto/create_image.html#step-2-image-creation)
- [Verify Image creation](/howto/create_image.html#step-3-verify-image-creation)

There are three steps to create a new server from an image:

- [Name your server](/howto/create_image.html#step-1-name-you-server)
- [Choose your Image](/howto/create_image.html#step-2-choose-your-image)
- [Create your server](/howto/create_image.html#step-3-create-your-server)


## Create an Image

In the Control Panel, click "Snapshot" in the compute section.

### Step 1 - Create an Image from a volume snapshot

On the page you land, are displayed the list of your snapshots.

![Snapshots list](../../images/create_image_from_snapshot.png "Snapshots list")

Select the snapshot to use for create an Image and click "Image from snapshot" button

### Step 2 - Image creation

You are now asked to give a name to your Image

![Create new Image](../../images/create_image.png "Create new Image")

Click the "Create Image" buttons, your Image is now ready to use.

### Step 3 - Verify Image creation

In the Compute section of the console click "Images". Your new Image should be present on Images list.

![Image details](../../images/image_details.png "Image details")

## Create a server from your own image

In the previous steps, we create a new Image.
We will create a new server based on the Image we take previously.

In the Control Panel, click the "Create Server" button.

###  Step 1 - Name you server

You will land on the server-creation page where you must input basic information for your server.

### Step 2 - Choose your Image

In the Image section click the Images tab.
Select the Image you take previously from the list below.

### Step 3 - Create your server

Click the "Create Server" button. This action starts your server. In a few seconds, your server will be ready to use.

The running server will be a template from your image.

