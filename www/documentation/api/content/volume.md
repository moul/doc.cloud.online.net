### group Volumes resources

This resources of API methods allows you to create, manage or delete your volumes.

#### Operation on a collection of volumes [/volumes]

##### Create a new volume [POST]

+ Parameters
    + name (required, string, `volume-0-3`)... The volume name
    + organization (required, string, `000a115d-2852-4b0a-9ce8-47f1134ba95a`)... Unique organization identifier
    + volume_type (required, string, `l_hdd`)... The volume type l_hdd or l_ssd
    + size (required, integer, `10000000000`) The volume size

+ Request (application/json)

    + Body
        {
          "name": "volume-0-3",
          "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
          "size": 10000000000,
          "volume_type": "l_ssd"
        }

+ Response 201
 
    + Headers (application/json)
                
            https://api.cloud.online.net/volumes/c675f420-cfeb-48ff-ba2a-9d2a4dbe3fcd

    + Body

            {
              "volume": {
                "export_uri": null, 
                "id": "c675f420-cfeb-48ff-ba2a-9d2a4dbe3fcd", 
                "name": "volume-0-3", 
                "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a", 
                "server": null, 
                "size": 10000000000, 
                "volume_type": "l_ssd"
              }
            }


##### Retrieves the list all existing volumes [GET]

+ Response 200 (application/json)

    {
      "volumes": [
        {
          "export_uri": null,
          "id": "f929fe39-63f8-4be8-a80e-1e9c8ae22a76",
          "name": "volume-0-1",
          "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
          "server": null,
          "size": 10000000000,
          "volume_type": "l_hdd"
        },
        {
          "export_uri": null,
          "id": "0facb6b5-b117-441a-81c1-f28b1d723779",
          "name": "volume-0-2",
          "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
          "server": null,
          "size": 20000000000,
          "volume_type": "l_ssd"
        }
      ]
    }


#### Operation on a single volume [/volumes/{volume_id}]

+ Parameters
    + volume_id (required, string, `f929fe39-63f8-4be8-a80e-1e9c8ae22a76`)... Volume unique identifier

##### Retrieves informations about a volume [GET]

+ Response 200 (application/json)

    {
      "volume": {
        "export_uri": null,
        "id": "f929fe39-63f8-4be8-a80e-1e9c8ae22a76",
        "name": "volume-0-1",
        "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
        "server": null,
        "size": 10000000000,
        "volume_type": "l_hdd"
      }
    }


##### Delete a volume [DELETE]

+ Response 204




