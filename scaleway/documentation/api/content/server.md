### group Servers resources

This resources of API methods allows you to create, manage or delete your servers

#### Servers [/servers]

##### Creates a new server [POST]

+ Parameters
    
    + name (required, string, `my_server`)... The server name
    + organization (required, string, `22222222-1111-4111-8111-222222222222`)... Organization unique identifier
    + image (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Image unique identifier
    + volumes (required, list, `[OUTDATED]`)... A list of volumes identifier to be attach to the server
    + tags (optional, list, `[test, www]`)... A list of tags
    + public_ip (optional, string, `4j6b46e4-edc2-32da-8ba6-dc5f853243tw`)... Id of reserved ip
    + dynamic_public_ip (optional, bool, `True`)... Boolean to assign or not a dynamic public IP

+ Request (application/json)

    + Body

            {
                TODO
            }

+ Response 201 (application/json)

        {
            TODO
        }

+ Response 400

+ Response 401

##### List all servers [GET]
Retrieve a list of servers with all their details

+ Response 200 (application/json)

        {
            
        }

+ Response 401

+ Response 

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
