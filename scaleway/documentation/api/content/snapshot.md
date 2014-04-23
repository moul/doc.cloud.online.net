### group Snapshots
Resources related to snapshots

#### Snapshots Collection [/snapshots]
A collection of snapshots with all their details

##### Create a snapshot [POST]
Create a new snapshot

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### List all snapshots [GET]
Retrieve a list of volumes with all their details

+ Response 200 (application/json)

        {
            
        }


#### Snapshot [/snapshots/{snapshot_id}]
A single snapshot with all its details

+ Parameters

    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier

##### Retrieve a snapshot [GET]
Retrieve details about a snapshot

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Update details about a snapshot [PUT]

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a snapshot [DELETE]

+ Response 204

+ Response 404

