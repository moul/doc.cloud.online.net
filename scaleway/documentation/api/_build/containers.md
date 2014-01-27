

###group Containers
#resources related to scaleway Containers.
####List containers [/containers?limit]
Retrieves containers granted for current user
#####[GET]

+ Parameters
	+ limit (required, string)... Maximum number of objects, default value is 10

####Create container [/containers]
Creates and provisions a new container
#####[POST]

+ Parameters

####Container info [/containers/{container_id}]
Retrieves detailed info about a container
#####[GET]

+ Parameters
	+ container_id (required, string)... Container unique identifier

####Edit container [/containers/{container_id}]
Updates info of a container
#####[PUT]

+ Parameters
	+ container_id (required, string)... Container unique identifier

####Delete container [/containers/{container_id}]
Deletes and deprovisions a container
#####[DELETE]

+ Parameters
	+ container_id (required, string)... Container unique identifier

####List container objects [/containers/{container_id}/objects?limit]
Retrieves container objects
#####[GET]

+ Parameters
	+ container_id (required, string)... Container unique identifier
	+ limit (required, string)... Maximum number of objects, default value is 10

####Create container object [/containers/{container_id}/objects]
Creates a new object in a container
#####[POST]

+ Parameters
	+ container_id (required, string)... Container unique identifier

####Container object info [/containers/{container_id}/objects/{object_id}]
Retrieves detailed info about a container object
#####[GET]

+ Parameters
	+ container_id (required, string)... Container object unique identifier
	+ object_id (required, string)... Container object path

####Edit container object [/containers/{container_id}/objects/{object_id}]
Updates info of a container
#####[PUT]

+ Parameters
	+ container_id (required, string)... Container unique identifier
	+ object_id (required, string)... Container object path

####Delete container object [/containers/{container_id}/objects/{object_id}]
Deletes and deprovisions a container
#####[DELETE]

+ Parameters
	+ container_id (required, string)... Container unique identifier
	+ object_id (required, string)... Container object path

