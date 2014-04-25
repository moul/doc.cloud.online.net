### group IPs resources

This resources of API methods allows you to create, manage or delete your reserved IPs.

#### Operation on a collection of IPs [/ips]

##### Create a new IP [POST]
Create a new IP

+ Parameters
    + organization (required, string, `f030e920-9743-4f28-8164-964ba8555fa5`)... Organization unique identifier

+ Request (application/json)

    + Body

            {
                "organization": "f030e920-9743-4f28-8164-964ba8555fa5"
            }

+ Response 201 (application/json)

        {
            TODO
        }

+ Response 400

+ Response 401

+ Response 403

##### Retrieves the list all existing IPs [GET]

+ Response 200 (application/json)

        {
            TODO   
        }

+ Response 401

+ Response 403

#### Operation on a single IP [/ips/{ip_address}]

+ Parameters
    + ip_address (required, string, `w.x.y.z`)... Ip address

##### Retrieves informations about an IP [GET]

+ Response 200 (application/json)

        {
            TODO
        }

+ Response 401

+ Response 403

+ Response 404

##### Update informations about an IP [PUT]

+ Parameters
    + ip_address (required, string, `w.x.y.z`)... Ip address
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

##### Remove an IP address [DELETE]

+ Response 204

+ Response 403

+ Response 404

