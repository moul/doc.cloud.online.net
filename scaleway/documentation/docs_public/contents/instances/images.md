---
title: Instance images
template: article.jade
---

#### Intro

Scaleway images are really usefull if you want to clone an instance to another or to publish an instance image to the market place.

Here's how to create your instance image

#### Sign in

In a first time go to the [Scaleway dashboard](xxx) and log in with your email and password.

Then, click on the “Servers” button on the left sidebar

### Create an image

#### Step 1 - Select your instance

From the list, select the instance that you want to create an image.

Once on the instance details page, on the submenu, click create an instance image.

#### Step 2 - Image creation

A popup appear before the operation start and you are asked for:

- Image name

The name of your image: It can be from 1 to 64 charaters without symblos

- Image description

The description of your image: 255 Unicode characters

- Volume you want to snapshot

The volume added to your image, you can add or remove volumes from the image except the system volumes

##### Optionnals

- No reboot

Instance image is create without rebooting your server

- Market place image

The image will be available publicly on the Image Market Place, by default, image are not published to the market place.

#### Step 3 - Save

Once you have selected all of your options, click on "Create Image." In the minutes that follows, your image will be set up and ready to use.

### Launch an image

#### Step 1 - Select your image

From the leftside menu click "Images" button.

Your list of images will appear, then select the image you want to use for your new instance and run it by clicking "Launch".

#### Step 2 - Set up instance

You land on the instance settings page and are asked to:

- Name your instance

The name of your instace: It can be from 1 to 64 charaters without symblos

- Tags your instance

To help you to manage your instances, and other resources, you can assign your own metadata to each resource in the form of tags. A tags as is a string with the following restrictions :

	- Maximum number of tags per resource: 10
	- Maximum length: 255 Unicode characters

- Choose security group

A security group acts as a firewall that controls the traffic for one or more instances.

#### Step 3 - Launch instance

Launch it, in few minutes your instance based on the selected image will appear on your server list.

### Delete an image

#### Step 1 - Select your image

From the leftside menu click "Images" button.

Your list of images will appear, then select the image you want to delete by clicking "Delete" on the submenu.

#### Step 2 - Set up instance

You are asked to confirm the deletion of the image, once confirmed the image will be delete.


#### Potential Uses

- Duplicate Server

- Automate Server Builds

- Create a Software Testing Environment

