### group Servers resources

This resources of API methods allows you to create, manage or delete your servers

#### Servers [/servers]

##### Creates a new server [POST]

+ Parameters
    
    + name (required, string, `my_server`)... The server name
    + organization (required, string, `f030e920-9743-4f28-8164-964ba8555fa5`)... Organization unique identifier
    + image (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Image unique identifier
    + volumes (required, list, `[OUTDATED]`)... A list of volumes identifier to be attach to the server
    + tags (optional, list, `[test, www]`)... A list of tags
    + public_ip (optional, string, `4j6b46e4-edc2-32da-8ba6-dc5f853243tw`)... Id of reserved ip
    + dynamic_public_ip (optional, bool, `True`)... Boolean to assign or not a dynamic public IP

+ Request (application/json)

    + Body

            {
                "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
                "name": "my_server",
                "image": "4e0b46e4-7c1d-44d4-8ba6-dc5f80694397"
            }

+ Response 201 (application/json)

        {
            
        }

+ Response 400

+ Response 401

##### List all servers [GET]
Retrieve a list of servers with all their details

+ Response 200 (application/json)

        {
          "servers": [
            {
              "dynamic_public_ip": false,
              "id": "442988e3-6c0e-4711-b3b2-3ba311cb722b",
              "image": null,
              "name": "Server-0-0",
              "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "f56af4c9-d902-4a17-88d6-a0a03f2c28c0",
                  "name": "Volume-0-0-0"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "e03b16fe-2300-4c1a-8b75-d42e7e4117b5",
              "image": null,
              "name": "Server-1-0",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "674e6ba2-8dc6-4a33-9dc2-832ef2c9ccf6",
                  "name": "Volume-1-0-0"
                },
                {
                  "id": "57d54a3b-6e3a-4ffc-a027-4d99761974eb",
                  "name": "Volume-1-0-1"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "f36f19a4-064b-4b9f-a713-62fa4594ee9d",
              "image": null,
              "name": "Server-1-1",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "7d3ed07e-3d97-424f-88a7-186e03cbcf6f",
                  "name": "Volume-1-1-0"
                },
                {
                  "id": "de4fc1ac-5f3a-4b78-b384-6303a2c66be8",
                  "name": "Volume-1-1-1"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "fa69a222-0e96-4110-a848-b0dca52fef4b",
              "image": null,
              "name": "Server-1-2",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "bad2ca11-4065-4e10-9f89-9fd25900b688",
                  "name": "Volume-1-2-0"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "73bcaa6d-e4c8-4bdb-8516-46d494dbccca",
              "image": null,
              "name": "Server-1-3",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "e49e5ee1-4cc5-444b-a9c4-fb1f71849cd1",
                  "name": "Volume-1-3-0"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "11edbb6d-d397-44df-9e29-9b7e74b51f15",
              "image": null,
              "name": "Server-1-4",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "83dd64fd-5d5b-4cdf-a4d1-c242878b98ab",
                  "name": "Volume-1-4-0"
                },
                {
                  "id": "948b4f63-04b6-4963-9264-308ba437d47f",
                  "name": "Volume-1-4-1"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "310f834c-1390-44f5-8646-13dd99735af3",
              "image": null,
              "name": "Server-1-5",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "7755910d-b54b-490f-b4a6-bad081a6edbb",
                  "name": "Volume-1-5-0"
                },
                {
                  "id": "83b73e77-05e3-4e83-b891-0d367f280072",
                  "name": "Volume-1-5-1"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "04e2900a-bd11-4076-8559-159101368c8b",
              "image": null,
              "name": "Server-1-6",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "cced9dfb-31d4-4191-b259-ac76e3912eea",
                  "name": "Volume-1-6-0"
                }
              ]
            },
            {
              "dynamic_public_ip": false,
              "id": "1b92c623-47df-4a4a-aed2-41210e7a0c75",
              "image": null,
              "name": "Server-1-7",
              "organization": "f1350c5d-f1d8-4f9d-b114-6053905578e1",
              "private_ip": null,
              "public_ip": null,
              "running": false,
              "tags": [],
              "volumes": [
                {
                  "id": "a029be85-d01f-48ca-992a-f0fbd87f4281",
                  "name": "Volume-1-7-0"
                }
              ]
            }
          ]
        }

+ Response 401

+ Response 

#### Server [/servers/{server_id}]
A single server with all its details

+ Parameters

    + server_id (required, string, `442988e3-6c0e-4711-b3b2-3ba311cb722b`)... Server unique identifier

##### Retrieve a server [GET]
Retrieve details about a server

+ Response 200 (application/json)

        {
          "server": {
            "dynamic_public_ip": false,
            "id": "442988e3-6c0e-4711-b3b2-3ba311cb722b",
            "image": null,
            "name": "Server-0-0",
            "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
            "private_ip": null,
            "public_ip": null,
            "running": false,
            "tags": [],
            "volumes": [
              {
                "id": "f56af4c9-d902-4a17-88d6-a0a03f2c28c0",
                "name": "Volume-0-0-0"
              }
            ]
          }
        }

+ Response 404

##### Update server [PUT]
Update details about a server

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove a server [DELETE]

+ Response 204

+ Response 404

#### Servers actions [/servers/{server_id}/action]
A collection of actions to be applied on a server

+ Parameters

    + server_id (required, string, `442988e3-6c0e-4711-b3b2-3ba311cb722b`)... Server unique identifier

##### Retrieve available actions list for a server [GET]

+ Response 200 (application/json)
     
        {
          "actions": [
            "poweron",
            "poweroff",
            "resetsoft",
            "resethard",
            "backup",
            "restore"
          ]
        }

##### Apply an action on a server [POST]

+ Response 20x (application/json)
     
        {
           
        }
