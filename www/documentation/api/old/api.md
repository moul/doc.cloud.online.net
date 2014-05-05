FORMAT: 1A


#Welcome to the Scaleway API documentation. This API provides access to Scaleway services.

##Request and response 

the scaleway api works over https and is accessed from the `api.scaleway.com` domain.

all data is sent and received as json.

## Constructing Requests

Requests are made of two components:

- API version
- Resource path

To construct a proper request, you will need to format the URI as follows:

`https://api.scaleway.com/{version}/{ressource}`

An example request, to retrieves detailed informations about an instance might be:

```
$curl -i https://api.scaleway.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Status: 200 OK
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
X-RateLimit-Reset: 1389359739
...

{
  "server": {
    "id": xxxx,
    "image_id": yyyy,
    "name": "zzzz",
    ...
  }
}
```


##Error

Scaleway uses conventional HTTP response codes to indicate success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that resulted from the provided information (e.g. a required parameter was missing, a charge failed, etc.), and codes in the 5xx range indicate an error with Scaleway's servers.


###HTTP Status Code Summary

- 200 OK - Everything worked as expected.
- 400 Bad Request - Often missing a required parameter.
- 401 Unauthorized - No valid API key provided.
- 402 Request Failed - Parameters were valid but request failed.
- 404 Not Found - The requested item doesn't exist.
- 500, 502, 503, 504 Server errors - something went wrong on Scaleway's end.

Not all errors map cleanly onto HTTP response codes, however. When a request is valid but does not complete successfully (e.g. an instance can not be launch), we return a 402 error code.

###Attributes

- type:
 - invalid_request_error: Occured when your request has an invalid parameters
 - api_error: API errors is used in case of problem with Scaleway's servers
- message:
 - A human readable error giving more details about the error
- code (Optional):
 - For ressources errors, it's a short string describing error that occurred.
- param (Optional):
 - The parameter the error relates to if the error is parameter-specific.


###Pagination

Methods returning multiple items are paginated to 25 items by default.
You can specify further pages with the ?page parameter. You can also set a custom page size up to 500 with the ?limit parameter.

```
$curl -i https://api.scaleway.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=5&limit=150

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Status: 200 OK
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
X-RateLimit-Reset: 1389359739
Link: <https://api.scaleway.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=1&limit=150>; rel="first", <https://api.scaleway.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=4&limit=150>; rel="prev", <https://api.scaleway.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=6&limit=150>; rel="next", <https://api.scaleway.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=10&limit=150>; rel="last",
...

{
  "tags": {
    ...
  }
}
```

##Resources




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



###group Volumes
#resources related to scaleway Volumes.
####List volumes [/volumes]
Lists volumes
#####[GET]

+ Parameters

####Create volume [/volumes]
Creates a new volume<br />This creates a volume. Volume is not attached by default.
#####[POST]

+ Parameters
	+ size (integer) (required, string)... the size of the volume to create
	+ base_volume (string) (required, string)... the id of the base volume
	+ base_snapshot (string) (required, string)... the id of the base snapshot
	+ type (string) (required, string)... the type of the volume

####Volume info [/volumes/{volume_id}]
Retrieves detailed info about a volume
#####[GET]

+ Parameters
	+ volume_id (required, string)... Volume unique identifier



###group Tags
#resources related to scaleway Tags.
####List tags [/tags?limit&server_id&name]
Retrieves tags granted for user<br />Retrieves tags and associated metadatas
#####[GET]

+ Parameters
	+ limit (required, string)... Maximum number of objects, default value is 100
	+ server_id (required, string)... Filter tags attached to an server
	+ name (required, string)... Filter by tag name

####Tag info [/tags/{tag_id}]
Retrieves detailed info about a tag
#####[GET]

+ Parameters
	+ tag_id (required, string)... Tag unique identifier

####Add tag [/tags]
Creates and provisions a new tag
#####[POST]

+ Parameters

####Edit tag [/tags/{tag_id}]
Updates info of a tag
#####[PUT]

+ Parameters
	+ tag_id (required, string)... tag unique identifier

####Delete tag [/tags/{tag_id}]
Deletes and deprovisions a tag
#####[DELETE]

+ Parameters
	+ tag_id (required, string)... Tag unique identifier

####List tag metadata [/tags/{tag_id}/metadatas?limit]
Retrieves tags granted for user
#####[GET]

+ Parameters
	+ tag_id (required, string)... Container unique identifier
	+ limit (required, string)... Maximum number of objects, default value is 100
	+ key (required, string)... Filter by key

####Create tag metadata [/tags/{tag_id}/metadatas]
Creates metadata
#####[POST]

+ Parameters
	+ tag_id (required, string)... Container unique identifier
	+ metadata_key (required, string)... Metadata key
	+ metadata_value (required, string)... New metadata value

####Update tag metadata [/tags/{tag_id}/metadatas/{metadata_key}]
Updates info of a container
#####[PUT]

+ Parameters
	+ tag_id (required, string)... Container unique identifier
	+ metadata_key (required, string)... Metadata key
	+ metadata_value (required, string)... New metadata value

####Delete tag metadata [/tags/{tag_id}/metadatas/{metadata_key}]
Deletes and deprovisions a tag
#####[DELETE]

+ Parameters
	+ tag_id (required, string)... Tag unique identifier
	+ metadata_key (required, string)... Metadata key



###group Organizations
#resources related to scaleway Organizations.
####List organizations [/organizations]
Retrieves full details of all organizations.
#####[GET]

+ Parameters

####List a summary of organizations [/organizations/summary]
Retrieves a list of IDs, names and levels of all organizations.
#####[GET]

+ Parameters

####Add organization [/organizations]
Create a new organization.
#####[POST]

+ Parameters
	+ name (string) (required, string)... organization name
	+ address_line1 (string) (required, string)... 
	+ address_zip (string) (required, string)... 
	+ address_city (string) (required, string)... 
	+ address_country (string) (required, string)... 
	+ technical_contacts (required, string)... list of technical contacts ids
	+ administrative_contacts (required, string)... list of administrative contacts ids
	+ billing_contacts (required, string)... list of billing contacts ids
	+ address_line2 (string) (required, string)... 
	+ address_state (string) (required, string)... 

####Get organization [/organizations/{id}]
Get all information about an organization.
#####[GET]

+ Parameters
	+ id (UUID) (required, string)... Organization unique ID

####Edit or update organization [/organizations/{id}]
Edit/update an organization.
#####[PUT]

+ Parameters
	+ id (UUID) (required, string)... Organization unique ID
	+ name (string) (required, string)... organization name
	+ technical_contacts (required, string)... list of technical contacts ids
	+ administrative_contacts (required, string)... list of administrative contacts ids
	+ billing_contacts (required, string)... list of billing contacts ids
	+ address_line1 (string) (required, string)... 
	+ address_line2 (string) (required, string)... 
	+ address_zip (string) (required, string)... 
	+ address_state (string) (required, string)... 
	+ address_city (string) (required, string)... 
	+ address_country (string) (required, string)... 

####Delete organization [/organizations/{id}]
Delete an organization
#####[DELETE]

+ Parameters
	+ id (UUID) (required, string)... Organization unique ID

