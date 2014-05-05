### group Object storage resources

This resources of API methods allows you to manage object storage.

#### Operation on a collection of containers [/containers]

##### Create a new container [POST]
Create a new container

+ Parameters
    + TODO (required, string, `TODO`)... TODO

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### Retrieves the list all existing containers [GET]

+ Response 200 (application/json)

        {
            TODO   
        }

+ Response 401

+ Response 403

#### Operation on a single container [/containers/{container_id}]

+ Parameters
    + container_id (required, string, `cid`)... Container unique identifier

##### Retrieves informations about an container [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Update details about a Container [PUT]

+ Parameters
    + container_id (required, string, `cid`)... Container unique identifier
    + TODO (required, string, `TODO`)... TODO

+ Request (application/json)

    + Body

            {
                TODO
            }


+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Remove a Container [DELETE]

+ Response 204

+ Response 403

+ Response 404

#### Operation on a file in a container [/containers/{container_id}/{path}]

+ Parameters
    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path

##### Retrieves informations about a file [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Update details about a file [PUT]

+ Parameters
    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path
    + TODO (required, string, `TODO`)... TODO    

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a file [DELETE]

+ Response 204

+ Response 403

+ Response 404

#### Download a file [/containers/{container_id}/dowload/{path}]

+ Parameters

    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path

##### Download the file present in the specified container [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 403

+ Response 404

#### Upload a file in the specified container [/containers/{container_id}/upload/{path}]

+ Parameters

    + path (required, string, `toto.txt`)... File path
    + container_id (required, string, `cid`)... File path
    + TODO (required, string, `TODO`)... TODO    

##### Upload the file in the specified container [POST]

+ Request (application/json)

    + Body

            {
                TODO
            }


+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404




