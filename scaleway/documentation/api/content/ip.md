### group IPs
Resources related to IPs

#### IPs Collection [/ips]
A collection of IPs with all their details

##### Create a new IP [POST]
Create a new IP

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### List all IP [GET]
Retrieve a list of IP with all their details

+ Response 200 (application/json)

        {
            
        }


#### IP [/ips/{ip_address}]
A single IP with all its details

+ Parameters

    + ip_address (required, string, `w.x.y.z`)... Ip address

##### Retrieve an IP [GET]
Retrieve details about a IP address

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Update details about an IP [PUT]

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove an IP address [DELETE]

+ Response 204

+ Response 404

