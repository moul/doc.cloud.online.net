### group Servers
Resources related to servers

#### Servers Collection [/servers]
A collection of servers with all their details

##### Create a server [POST]
Create a new server

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### List all servers [GET]
Retrieve a list of servers with all their details

+ Response 200 (application/json)

        {
            
        }

#### Server [/servers/{server_id}]
A single server with all its details

+ Parameters

    + server_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Server unique identifier

##### Retrieve a server [GET]
Retrieve details about a server

+ Response 200 (application/json)

        {
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

    + server_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Server unique identifier

##### Retrieve available actions list for a server [GET]

+ Response 200 (application/json)
     
        {
           
        }

##### Apply an action on a server [POST]

+ Response 20x (application/json)
     
        {
           
        }
