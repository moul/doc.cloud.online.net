---
title: User browsing
template: article.jade
---

####Login register user

A register user arrive on hyperscale.com and click signin button || A register user arrive on console.hyperscale.com

- User has to type a login
- User has to type a password
- User has to click the login button
- User is redirect to the HyperScale console

####Server creation

*User must be logged

- Case 1 (from console homepage):
	- User click create server on the right side menu
- Case 2 (from the right menu)
	- User click on the top right (+new server)
- Page change to new server
- User has to select an organization
- User has to type the server name
- User has top type tags for server
- User choose an image
	- User can select his own images
	- User can select images from the marketplace
	- User can select images from previous snapshot
- Add volumes
	- Case 1 new volume
		- The user type the name of the volume
		- The user choose the type of volume (Scalable distribued storage or Low latency)
		- The user type the size of the volume
		- The user click create a new volume
	- Case 2 (existing volume) -The user click add existing volume
		- A popin display the list of existing volumes
		- The user select (multi-select) the volumes to add
		- The user click ok / cancel

####Servers listing

*User must be logged

- Case 1 (From the servers menu)
	- User click Servers on the right side menu
- Case 2 (From console homepage)
	- User click on Running instance block
- Case 3 (From console homepage)
	- User click on Server block
- User servers list is displayed (Name, IP, Tags, State)
- User can filter servers list by using Search server input
- User can change state of a server (ON/OFF)
- User can click on a server (The page change to server details)
	- Server details are displayed (Server id, name, ip address, volumes, tags)
		- User can change server state by clicking (ON / OFF) on the top right
		- User can edit a server
			- User can click edit button
			- User can change server name
			- User can change server tags
			- User can save or cancel changes
		- User can click more and delete server
			- A popin appear asking for confirmation

####Volume creation

*User must be logged

- User click volumes on the top right menu
- User click +New volume
- User has to create a new volume or create from existing one
- Case 1 (Create new volume)
	- User choose a name for the volume
	- User type a size for the volume
	- User choose the type of volume (Scalable distribued storage or Low latency)
	- User click create new volume button
- Case 2 (Create from existing volume)
	- User choose which volume he want to import
	- User choose a name for the volume
	- User choose the type of volume (Scalable distribued storage or Low latency)
	- User click create new volume from existing button

####Volumes listing

*User must be logged

- Case 1 (From the right menu)
	- User click Volumes on the right side menu
Case 2 (From console homepage):
	- User click on Volumes block
- Volumes list is displayed (Name, type, size, server using it)
- User can filter volumes list by using Search volumes input
- User can click on a volume
	- Volume details are displayed (Volume id, name, size, type, server using it)
		- The user can click more and delete a volume
			- A popin appear asking for confirmation

####Create a bucket

*User must be logged

- User click Files on the right side menu
- User click "Create bucket" button
- A popin appear asking for bucket name
- Bucket appear in the buckets list

####Buckets listing

*User must be logged

- User click Files on the right side menu
- User buckets list is displayed (Bucket name, files number, Delete button)
- User can delete a bucket
	- A popin appear asking for confirmation
- User can click on a bucket
	- Files inside the bucket are listed (Filename, Size, Download button, Delete button)
	- User can download a file
	- User can delete a file
		- A popin appear asking for confirmation
	- User can add files to the bucket
		- User drop a file(s) into the "drop files here" zone

####Create an organization

*User must be logged

- User click on organization menu
- User click on "Create an organization"
