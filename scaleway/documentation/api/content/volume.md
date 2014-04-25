### group Volumes resources

This resources of API methods allows you to create, manage or delete your volumes.

#### Operation on a collection of volumes [/volumes]

##### Create a new volume [POST]

+ Parameters
    + organization (required, string, `f030e920-9743-4f28-8164-964ba8555fa5`)... Unique organization identifier
    + name (required, string, `Volume-1-8-0`)... Human readable volume name
    + volume_type (required, string, `l_hdd`)... The volume type l_hdd or l_ssd
    + size (required, integer, `50000000000`) The volume size

+ Request (application/json)

    + Body

            {
                "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
                "name": "Volume-1-8-0",
                "volume_type": "l_hdd",
                "size": 50000000000
            }

+ Response 201
 
    + Headers (application/json)
                
                location: http://127.0.0.1:5002/volumes/3c822cfb-19ea-49ba-8891-9cfaabac0255

    + Body
          
            {
                "volume": {
                    "export_uri": null,
                    "id": "3c822cfb-19ea-49ba-8891-9cfaabac0255",
                    "name": "Volume-1-8-0",
                    "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
                    "server": null,
                    "size": 50000000000,
                    "volume_type": "l_hdd"
                  }
            }

+ Response 400

+ Response 401

+ Response 403

##### Retrieves the list all existing volumes [GET]

+ Response 200 (application/json)

      {
          "volumes": [
            {
              "export_uri": null,
              "id": "7d3ed07e-3d97-424f-88a7-186e03cbcf6f",
              "name": "Volume-1-1-0",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "server": {
                "id": "f36f19a4-064b-4b9f-a713-62fa4594ee9d",
                "name": "Server-1-1"
              },
              "size": 50000000000,
              "volume_type": "l_hdd"
            },
            {
              "export_uri": null,
              "id": "de4fc1ac-5f3a-4b78-b384-6303a2c66be8",
              "name": "Volume-1-1-1",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "server": {
                "id": "f36f19a4-064b-4b9f-a713-62fa4594ee9d",
                "name": "Server-1-1"
              },
              "size": 50000000000,
              "volume_type": "l_hdd"
            },
            {
              "export_uri": null,
              "id": "e49e5ee1-4cc5-444b-a9c4-fb1f71849cd1",
              "name": "Volume-1-3-0",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "server": {
                "id": "73bcaa6d-e4c8-4bdb-8516-46d494dbccca",
                "name": "Server-1-3"
              },
              "size": 50000000000,
              "volume_type": "l_hdd"
            },
            {
              "export_uri": null,
              "id": "83dd64fd-5d5b-4cdf-a4d1-c242878b98ab",
              "name": "Volume-1-4-0",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "server": {
                "id": "11edbb6d-d397-44df-9e29-9b7e74b51f15",
                "name": "Server-1-4"
              },
              "size": 50000000000,
              "volume_type": "l_hdd"
            },
            {
              "export_uri": null,
              "id": "7755910d-b54b-490f-b4a6-bad081a6edbb",
              "name": "Volume-1-5-0",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "server": {
                "id": "310f834c-1390-44f5-8646-13dd99735af3",
                "name": "Server-1-5"
              },
              "size": 50000000000,
              "volume_type": "l_hdd"
            }
          ]
        }

+ Response 401

+ Response 403

#### Operation on a single volume [/volumes/{volume_id}]

+ Parameters
    + volume_id (required, string, `8a8095d7-7db0-40c6-b867-0c0708f5e918`)... Volume unique identifier

##### Retrieves informations about a volume [GET]

+ Response 200 (application/json)

        {
            "volume": {
                "export_uri": null,
                "id": "f56af4c9-d902-4a17-88d6-a0a03f2c28c0",
                "name": "Volume-0-0-0",
                "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
                "server": null,
                "size": 50000000000,
                "volume_type": "l_hdd"
              }
        }

+ Response 401

+ Response 403

+ Response 404

##### Delete a volume [DELETE]

+ Response 204

+ Response 403

+ Response 404



