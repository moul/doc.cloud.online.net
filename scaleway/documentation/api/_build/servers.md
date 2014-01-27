

###group Servers
#resources related to scaleway Servers.
####Server list [/servers?limit&organization_id&image_id&ip]
Retrieves servers granted for current user
#####[GET]

+ Parameters
	+ limit (required, string)... Maximum number of objects, default value is 100
	+ organization (required, string)... Filter by organization
	+ image (required, string)... Filter by image

####Create server [/servers]
Creates and provisions a new server<br />This creates a server and also creates and assigns a default tag (type:server and name:default). Server has default state:off.
#####[POST]

+ Parameters
	+ volumes (list) (required, string)... A list of volumes to attach to the server which will be mounted as nbdX where X is there position in the list

####Server info [/servers/{server_id}]
Retrieves detailed info about a server
#####[GET]

+ Parameters
	+ server_id (required, string)... Server unique identifier

####Edit server [/servers/{server_id}]
Updates info of a server
#####[PUT]

+ Parameters
	+ server_id (required, string)... Server unique identifier

####Delete server [/servers/{server_id}]
Deletes and deprovisions a server
#####[DELETE]

+ Parameters
	+ server_id (required, string)... Server unique identifier

####List server actions [/servers/{server_id}/action]
Lists available actions for the specified server
#####[GET]

+ Parameters
	+ server_id (required, string)... Server unique identifier

####Run server action [/servers/{server_id}/action]
Runs an action on server
#####[POST]

+ Parameters
	+ server_id (required, string)... Server unique identifier
	+ action (required, string)... Action name (see list-server-actions)

####List server sessions [/servers/{server_id}/sessions?limit&active]
Retrieves server sessions
#####[GET]

+ Parameters
	+ server_id (required, string)... Server unique identifier
	+ limit (required, string)... Maximum number of objects, default value is 100
	+ active (required, string)... Filter by active, default is false

####Get server session info [/servers/{server_id}/sessions/{session_id}]
Retrieves detailed info about a server session
#####[GET]

+ Parameters
	+ server_id (required, string)... Server unique identifier
	+ session_id (required, string)... Server session unique identifier

####List server tags [/servers/{server_id}/tags?limit]
Retrieves attached tags list for a server
#####[GET]

+ Parameters
	+ server_id (required, string)... Server unique identifier
	+ limit (required, string)... Maximum number of objects, default value is 100

####Attach tag to server [/servers/{server_id}/tags]
Attachs tag to a server<br />Attach an already existing tag to a server
#####[POST]

+ Parameters
	+ server_id (required, string)... Server unique identifier

####Detach tag from server [/servers/{server_id}/tags/{tag_id}]
Detach tag from server
#####[DELETE]

+ Parameters
	+ server_id (required, string)... Server unique identifier
	+ tag_id (required, string)... Tag unique identifier

