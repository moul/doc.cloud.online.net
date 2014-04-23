### group Containers
Resources related to Containers

#### Containers Collection [/containers]
A collection of Containers with all their details

##### Create a new container [POST]
Create a new container

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### List all containers [GET]
Retrieve a list of Containers with all their details

+ Response 200 (application/json)

        {
            
        }

#### Container [/containers/{container_id}]
A single container with all its details

+ Parameters

    + container_id (required, string, `cid`)... Container unique identifier

##### Retrieve an Container [GET]
Retrieve details about a Container

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Update details about a Container [PUT]

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a Container [DELETE]

+ Response 204

+ Response 404


#### Path [/containers/{container_id}/{path}]
A single path with all its details

+ Parameters

    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path

##### Retrieve a file [GET]
Retrieve details about a file

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a file [DELETE]

+ Response 204

+ Response 404

##### Update details about a file [PUT]

+ Response 200 (application/json)

        {
        }

+ Response 404

#### Download file [/containers/{container_id}/dowload/{path}]

+ Parameters

    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path

##### Download a file [GET]

+ Response 200 (application/json)

        {
        }

+ Response 404

#### Upload file [/containers/{container_id}/upload/{path}]

+ Parameters

    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path

##### Upload a file [POST]

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401





