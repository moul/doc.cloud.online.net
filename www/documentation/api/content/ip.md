### group IPs resources

This resources of API methods allows you to create, manage or delete your reserved IPs.

#### Operation on a collection of IPs [/ips]

##### Create a new IP [POST]
Create a new IP

+ Parameters
    + organization (required, string, `000a115d-2852-4b0a-9ce8-47f1134ba95a`)... Organization unique identifier

+ Request (application/json)

    + Body

            {
                "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a"
            }

+ Response 201 (application/json)

            {
              "ip": {
                "address": "212.47.226.88",
                "id": "b50cd740-892d-47d3-8cbf-88510ef626e7",
                "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
                "server": null
              }
            }

##### Retrieves the list all existing IPs [GET]

+ Response 200 (application/json)

        {
          "ips": [
            {
              "address": "212.47.226.88",
              "id": "b50cd740-892d-47d3-8cbf-88510ef626e7",
              "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
              "server": null
            }
          ]
        }

#### Operation on a single IP [/ips/{ip_id}]

+ Parameters
    + ip_id (required, string, `b50cd740-892d-47d3-8cbf-88510ef626e7`)... Ip unique identifier

##### Retrieves informations about an IP [GET]

+ Response 200 (application/json)

        {
          "ip": {
            "address": "212.47.226.88",
            "id": "b50cd740-892d-47d3-8cbf-88510ef626e7",
            "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
            "server": null
          }
        }

##### Attach an IP [PUT]

+ Request (application/json)

    + Body

            {
                "address": "212.47.226.88",
                "id": "b50cd740-892d-47d3-8cbf-88510ef626e7",
                "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
                "server": "c2d8994f-1582-413e-8d48-c53076db06cc"
            }


+ Response 200 (application/json)

        {
          "ip": {
            "address": "212.47.226.88",
            "id": "b50cd740-892d-47d3-8cbf-88510ef626e7",
            "organization": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
            "server": {
              "id": "c2d8994f-1582-413e-8d48-c53076db06cc",
              "name": "default_server_name - acfb51"
            }
          }
        }


##### Remove an IP address [DELETE]

+ Response 204


