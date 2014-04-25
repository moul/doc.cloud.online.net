### group Tokens
Resources related to scaleway Tokens

#### Tokens Collection [/tokens]
A collection of tokens with all their details

##### Create a token [POST]
Create a new token for the specified user

+ Parameters
    + email (required, string, `general@ocs.online.net`)... User email
    + password (required, string, `password`)... User password
    + expires (optional, boolean, `false`)... Set if you want a token wich doesn't expire (default: true)

+ Request (application/json)

    + Body

            {
                "email": "general@ocs.online.net",
                "password": "password",
                "expires": false
            }

+ Response 201

    + Headers (application/json)
           
            location: http://127.0.0.1:5004/tokens/d16492ea-9d3b-449d-a2ff-dc907c33a1d0

    + Body

            {
              "token": {
                "creation_date": "2014-04-25T08:59:44.515484+00:00",
                "expires": "2014-04-25T11:29:44.803837+00:00",
                "id": "d16492ea-9d3b-449d-a2ff-dc907c33a1d0",
                "inherits_user_perms": true,
                "permissions": [],
                "roles": [],
                "user_id": "22222222-1111-4111-8111-111111111111"
              }
            }

+ Response 400

+ Response 401

##### List all Tokens [GET]
Retrieve a list of Tokens with all their details

+ Response 200 (application/json)

        {
            "tokens": [
                {
                    "creation_date": "2014-03-03T14:32:30.453191+00:00",
                    "expires": "2014-03-03T16:02:30.741487+00:00",
                    "id": "b8de98c2-3f87-40c7-8e34-4fc37b6a1b8a",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                },
                {
                    "creation_date": "2014-03-03T14:44:47.763145+00:00",
                    "expires": null,
                    "id": "4c518778-3831-4ed6-9d19-bcba66329b08",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                },
                {
                    "creation_date": "2014-03-03T13:41:31.763838+00:00",
                    "expires": "2014-03-03T16:16:45.672639+00:00",
                    "id": "1d020419-f0b4-4b15-89cd-b9c62c5d4fbb",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                }
            ]
        }

#### Token [/tokens/{token_id}]
A single token with all its details

+ Parameters
    + token_id (required, string, `67b231c5-69ca-442e-bee6-5ba2d9c98336`)... Token unique identifier

##### Retrieve a token [GET]
Retrieve details about a token

+ Response 200 (application/json)

        {
            "token": {
                "creation_date": "2014-03-03T13:41:31.763838+00:00",
                "expires": "2014-03-03T16:16:45.672639+00:00",
                "id": "1d020419-f0b4-4b15-89cd-b9c62c5d4fbb",
                "inherits_user_perms": true,
                "permissions": [],
                "roles": [],
                "user_id": "22222222-1111-4111-8111-111111111111"
            }
        }

+ Response 404

##### Update token [PATCH]
Increase token expiration time of 30 minutes

+ Response 200 (application/json)

        {
            "token": {
                "creation_date": "2014-03-03T13:41:31.763838+00:00",
                "expires": "2014-03-03T16:16:45.672639+00:00",
                "id": "1d020419-f0b4-4b15-89cd-b9c62c5d4fbb",
                "inherits_user_perms": true,
                "permissions": [],
                "roles": [],
                "user_id": "22222222-1111-4111-8111-111111111111"
            }
        }

+ Response 404

##### Remove a token [DELETE]

+ Response 204

+ Response 404

#### Token permissions [/tokens/{token_id}/permissions]
A collection of permissions for a specified token

+ Parameters
    + token_id (required, string, `67b231c5-69ca-442e-bee6-5ba2d9c98336`)... Token unique identifier

##### Retrieve token permissions [GET]

+ Response 200 (application/json)
     
        {
            "permissions": {
                "account": {
                    "organization:*": [
                        "11111111-1111-4111-8111-111111111111",
                        "22222222-1111-4111-8111-222222222222"
                    ],
                    "token:*": [
                        "22222222-1111-4111-8111-111111111111"
                    ],
                    "user:*": [
                        "22222222-1111-4111-8111-111111111111"
                    ],
                    "users:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ]
                },
                "compute": {
                    "images:*": [
                        "11111111-1111-4111-8111-111111111111:*",
                        "22222222-1111-4111-8111-222222222222:*"
                  ],
                  "ips:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                  ],
                  "security_groups:*": [
                        "11111111-1111-4111-8111-111111111111:*",
                        "22222222-1111-4111-8111-222222222222:*"
                  ],
                  "servers:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                  ],
                  "tasks:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                  ],
                  "volumes:*": [
                        "11111111-1111-4111-8111-111111111111:*",
                        "22222222-1111-4111-8111-222222222222:*"
                  ]
                },
                "dns": {
                    "dns:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ]
                },
                "storage": {
                    "storage:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ]
                },
                "ticket": {
                    "tickets:*": [
                        "22222222-1111-4111-8111-111111111111"
                    ]
                }
            }
        }

### group Organizations
Resources related to scaleway Organizations

#### Organizations Collection [/organizations]
A collection of Organization with all their details

##### List all Organizations [GET]
Retrieve a list of Organizations with all their details

+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "organizations": [
                {
                    "id": "22222222-1111-4111-8111-222222222222",
                    "name": "General Inc"
                },
                {
                    "id": "11111111-1111-4111-8111-111111111111",
                    "name": "HyperScale"
                }
            ]
        }

+ Response 401

#### Organization [/organizations/{organization_id}]
A single Organization with all its details

+ Parameters
    + organization_id (required, string, `22222222-1111-4111-8111-222222222222`)... Organization unique identifier

#### Retrieve an Organization [GET]
Retrieve details about an organization

+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "organization": {
                "id": "11111111-1111-4111-8111-111111111111",
                "name": "HyperScale"
            }
        }

+ Response 401

+ Response 404

#### Invitations Collection [/organizations/{organization_id}/invites]
A collection of invitations in a specified Organization


+ Parameters
    + organization_id (required, string, `22222222-1111-4111-8111-222222222222`)... Organization unique identifier

##### Create an invitation [POST]
Create an invitation for a new user in the specified organization

+ Parameters
    + organization_id (required, string, `22222222-1111-4111-8111-222222222222`)... Organization unique identifier
    + email (required, string, `mail@provider.ext`)... The email to send the invitation
    + firstname (required, string, `John`)... Invited user firstname
    + lastname (required, string, `Smith`)... Invited user lastname

+ Request (application/json)

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

    + Body

            {
                "email": "rh1@mail.ext",
                "firstname": "Rob",
                "lastname": "Hill"
            }

+ Response 201 (application/json)

        {
            "invite": {
                "email": "js@mail.ext",
                "firstname": "John",
                "id": "c91b2e74-864b-43b6-b96e-e7157e7cffeb",
                "lastname": "Smith",
                "status": "pending"
            }
        }

+ Response 400

+ Response 401

+ Response 404

##### List all invitations [GET]
Retrieve a list of invitations with all their details

+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "invites": [
                {
                    "email": "rh@mail.ext",
                    "firstname": "Rob",
                    "id": "c91b2e74-864b-43b6-b96e-e7157e7cffeb",
                    "lastname": "Hill",
                    "status": "pending"
                }
            ]
        }

+ Response 401

+ Response 404



### group Users
Resources related to scaleway Users

#### User [/users/{user_id}]
Retrieve informations for the specified user

+ Parameter
    + user_id (required, string, `22222222-1111-4111-8111-111111111111`)... User unique identifier

##### Retrieve a user [GET]
Retrieve details about a user


+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "user": {
                "email": "js@mail.ext",
                "firstname": "John",
                "fullname": "John Smith",
                "id": "22222222-1111-4111-8111-111111111111",
                "lastname": "Smith",
                "organizations": [
                    {
                        "id": "22222222-1111-4111-8111-222222222222",
                        "name": "General Inc"
                    },
                    {
                        "id": "11111111-1111-4111-8111-111111111111",
                        "name": "Scaleway"
                    }
                ],
                "roles": [
                    {
                        "organization": {
                            "id": "22222222-1111-4111-8111-222222222222",
                            "name": "General Inc"
                        },
                        "role": "admin"
                    },
                    {
                        "organization": {
                            "id": "11111111-1111-4111-8111-111111111111",
                            "name": "Scaleway"
                        },
                        "role": "admin"
                    },
                    {
                        "organization": {
                            "id": "11111111-1111-4111-8111-111111111111",
                            "name": "Scaleway"
                        },
                        "role": "super_admin"
                    }
                ],
                "ssh_public_keys": null
            }
        }

+ Response 401

+ Response 404




