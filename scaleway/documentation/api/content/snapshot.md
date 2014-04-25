### group Snapshots resources

This resources of API methods allows you to create, manage or delete your snapshots.

#### Operation on a collection of snapshots [/snapshots]

##### Create a snapshot [POST]

+ Parameters
    + name (required, string, ``)... Human readable snapshot name
    + organization (required, string, `f1350c5d-f1d8-4f9d-b114-6053905578e1`)... Unique organization identifier
    + volume_id (required, string, `de4fc1ac-5f3a-4b78-b384-6303a2c66be8`)... Unique volume identifier

+ Request (application/json)

    + Body

            {
                "name": "snapshot-0-1",
                "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
                "volume_id": "de4fc1ac-5f3a-4b78-b384-6303a2c66be8"
            }

+ Response 201 (application/json)

        {
          "snapshot": {
            "id": null,
            "name": "snapshot-0-1",
            "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
            "size": 50000000000,
            "state": "snapshotting",
            "volume_type": "l_hdd"
          }
        }

+ Response 400

+ Response 401

+ Response 403

##### Retrieves the list all existing snapshots [GET]

+ Response 200 (application/json)

        {
            "snapshots": []
        }

+ Response 401

+ Response 403

#### Operation on a single snapshot [/snapshots/{snapshot_id}]

+ Parameters
    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier

#####Retrieves informations about an snapshot [GET]

+ Response 200 (application/json)

        {
            "snapshots": {


            }
        }

+ Response 401

+ Response 403

+ Response 404

##### Update informations about an snapshot [PUT]

+ Parameters
    + snapshot_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Snapshot unique identifier
    + organization (required, string, `f1350c5d-f1d8-4f9d-b114-6053905578e1`)... Organization unique identifier

+ Request (application/json)

    + Body

            {
                "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1"
            }


+ Response 200 (application/json)

        {
            "snapshot": {
                "id": null,
                "name": "snapshot-0-1",
                "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
                "size": 50000000000,
                "state": "snapshotting",
                "volume_type": "l_hdd"
            }
        }

+ Response 401

+ Response 403

+ Response 404

##### Remove a snapshot [DELETE]

+ Response 204

+ Response 403

+ Response 404
