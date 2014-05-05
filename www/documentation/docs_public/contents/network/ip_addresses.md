---
title: IP Addresses
template: article.jade
position: 1
---

When you create an instance, we assign it a public IP address at launch.
By default, the public IP address associated with your instance is dynamic, that mean if you delete your instance you cannot reuse this IP address.

We also provide static IP address, like dynamic IP they are public but they act like a resource. They can be assigned to an instance, they are persistent and they can be remapped to any instance associated with your account.

This documentation will guide you through the process of managing reserved IP adresses.

### Step 1 - Allocate a reserved IP

Here is the process to allocate a new reserved IP and to attach it to an existing instance.

  1. Go to labs.online.net dashboard
  2. Click to the network menu on the right panel
  3. Click on Create new ip 
  4. Select the instance you want to attach the IP address

### Step 2 - Reassociate a reserved IP to another instance

  1. Go to labs.online.net dashboard
  2. Click to the network menu on the right panel
  3. The list of allocated IP addresses appear
  4. Select the ip you want to reassociate
  5. In the association dialog box, select the new instance to associate the IP

### Step 3 - Delete a reserved IP

  1. Go to labs.online.net dashboard
  2. Click to the network menu on the right panel
  3. The list of allocated IP addresses appear
  4. Select the ip wou want to delete
  5. Click on delete on the top left