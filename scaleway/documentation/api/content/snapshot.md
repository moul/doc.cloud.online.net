### group Snapshots resources

This resources of API methods allows you to create, manage or delete your snapshots.

#### Operation on a collection of snapshots [/snapshots]

##### Create a snapshot [POST]

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

##### Retrieves the list all existing snapshots [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

#### Operation on a single snapshot [/snapshots/{snapshot_id}]

+ Parameters
    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier

#####Retrieves informations about an snapshot [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Update informations about an snapshot [PUT]

+ Parameters
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

##### Remove a snapshot [DELETE]

+ Response 204

+ Response 403

+ Response 404
