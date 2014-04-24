### group Volumes resources

This resources of API methods allows you to create, manage or delete your volumes.

#### Operation on a collection of volumes [/volumes]

##### Create a new volume [POST]

+ Parameters
    + TODO (required, string, `TODO`)... TODO

+ Request (application/json)

    + Body

            {
                TODO
            }

+ Response 201 (application/json)

        {
            TODO
        }

+ Response 400

+ Response 401

+ Response 403

##### Retrieves the list all existing volumes [GET]

+ Response 200 (application/json)

        {
            TODO   
        }

+ Response 401

+ Response 403

#### Operation on a single volume [/volumes/{volume_id}]

+ Parameters
    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier

##### Retrieves informations about a volume [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Delete a volume [DELETE]

+ Response 204

+ Response 403

+ Response 404

#### Operation on a collection of snapshots associate to a volume [/volumes/{volume_id}/snapshots]


+ Parameters
    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier


##### Create a new snapshot for the volume [POST]

+ Parameters
    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier
    + TODO

+ Request (application/json)

    + Body

            {
                TODO
            }

+ Response 201 (application/json)

        {
            TODO
        }

+ Response 400

+ Response 401

+ Response 403

##### Retrieves the list all existing snapshots for the volume [GET]

+ Response 200 (application/json)
     
        {
           TODO
        }

+ Response 401

+ Response 403

+ Response 404

#### Operation on a single snapshot associate to a volume [/volumes/{volume_id}/snapshots/{snapshot_id}]

+ Parameters
    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier
    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier

##### Retrieves informations about a snapshot [GET]

+ Response 200 (application/json)
     
        {
           TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Update informations about a snapshot [PUT]

+ Parameters
    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier
    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier
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

##### Delete a snapshot [DELETE]

+ Response 204

+ Response 403

+ Response 404        



