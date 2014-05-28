---
title: Create your own image
template: article.jade
position: 3
---

This page shows you how to create an image from a server.

Requirements

- You have an labs.online.net account
- You have Setting up your ssh key
- You need to have at least a running server

An image is a kind of "Box" that includes one or more volumes containing the operating system (e.g., Linux) and any additional software required to deliver a service or a portion of it.<br/>

There are 4 steps to create an an image and spawn a server from it

- Power off your server
- Create an image
- Verify image creation

### Potential Uses

- Duplicate Server
- Automate Server Builds
- Create a Software Testing Environment


###Step 1 - Create image from a volume snapshot

Click on the "Images button on left-side menu, you will arrive on your images list.<br/>Are displayed the list of images available if they are. To create a new one click the "Create image" button

![Images list](../../images/images_list.png "Images list")

### Step 2 - Image creation

You are now asked for:

- Giving an image name

- Choose the volume snapshot you want to use for your image

![Create new image](../../images/create_new_image.png "Create-new-image")

Once achieve, click on "Create Image." In the minutes that follows, your image will be set up and ready to use.


### Coming soon

- No reboot - Instance image is create without rebooting your server
- Market place image - Image will be available publicly on the Image Market Place, by default, image are not published to the market place.
- Create an image directly from an instance
