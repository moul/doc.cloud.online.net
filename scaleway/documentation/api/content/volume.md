### group Volumes
Resources related to volumes

#### Volumes Collection [/volumes]
A collection of volumes with all their details

##### Create a volume [POST]
Create a new volume

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### List all volumes [GET]
Retrieve a list of volumes with all their details

+ Response 200 (application/json)

        {
            
        }


#### Volume [/volumes/{volume_id}]
A single volume with all its details

+ Parameters

    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Server unique identifier

##### Retrieve a volume [GET]
Retrieve details about a volume

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a volume [DELETE]

+ Response 204

+ Response 404

#### Snapshots [/volumes/{volume_id}/snapshots]
A collection of snapshots associate to a volume

+ Parameters

    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier

##### Retrieve list of snapshots [GET]

+ Response 200 (application/json)
     
        {
           
        }

##### Create a new snapshot [POST]

+ Response 20x (application/json)
     
        {
           
        }

#### Snapshot [/volumes/{volume_id}/snapshots/{snapshot_id}]
A single snapshot with all its details

+ Parameters

    + volume_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Volume unique identifier
    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier

##### Retrieve details about a snapshot [GET]

+ Response 200 (application/json)
     
        {
           
        }

##### Update details about a snapshot [PUT]

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a snapshot [DELETE]

+ Response 204

+ Response 404        



