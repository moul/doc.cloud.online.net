### group Organizations
Resources related to scaleway Organizations

#### List organizations [/organizations]
Retrieves organizations granted for current user
##### [GET]

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

+ Response 401 (application/json)

        {
            "message": "Invalid authentication token: 59517bee-4ccb-43fa-95d0-f52292aad10",
            "type": "invalid_auth"
        }

#### Get organization [/organizations/{organization_id}]
Retrieve details info about an organization
##### [GET]

+ Parameters

    + organization_id (required, string, `11111111-1111-4111-8111-111111111111`)... Organization unique identifier

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

+ Response 404 (application/json)

        {
            "message": "Organization not found",
            "type": "unknown_resource"
        }

#### Invite creation [/organizations/{organization_id}/invites]
Create an invitation for a new user in the specified organization
##### [POST]

+ Parameters

    + organization_id (required, string, `11111111-1111-4111-8111-111111111111`)... Organization unique identifier
    + email (required, string, `mail@provider.ext`)... The email to send the invitation
    + firstname (required, string, `John`)... Invited user firstname
    + lastname (required, string, `Smith`)... Invited user lastname

+ Request (application/json)

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

    + Body

            {
                "email": "rh@mail.ext",
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

+ Response 400 (plain/text)

    + Body

            You already sent all your invites.

+ Response 400 (application/json)

        {
            "fields": {
                "email": [
                    "incorrect email address",
                    "required key not provided"
                ],
                "firstname": [
                    "length of value must be at least 2",
                    "required key not provided"
                ],
                "lastname": [
                    "length of value must be at least 2",
                    "required key not provided"
                ]
            },
            "message": "Validation Error",
            "type": "invalid_request_error"
        }

+ Response 404 (application/json)

        {
            "message": "Organization not found",
            "type": "unknown_resource"
        }

#### Get invite [/organizations/{organization_id}/invites]
Retrieve invitations for a specified organization
##### [GET]

+ Parameters

    + organization_id (required, string, `11111111-1111-4111-8111-111111111111`)... Organization unique identifier

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

+ Response 404 (application/json)

        {
            "message": "Organization not found",
            "type": "unknown_resource"
        }

### group Tokens
resources related to scaleway Tokens

#### Create new token [/tokens]
Create a new token for specified user
##### [POST]

+ Parameters

    + email (required, string, `js@mail.ext`)... User email
    + password (required, string, `password`)... User password
    + expires (optional, boolean, `false`)... Set if you want a token wich doesn't expire (default: true)

+ Request (application/json)

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

    + Body

            {
                "email": "js@mail.ext",
                "password": "password",
                "expires": false
            }

+ Response 201 (application/json)

    + Headers

            Location: http://api.scaleway.com/v1/tokens/7db33cf3-b43b-4457-aaf7-ac7c7fae378e

    + Body

            {
                "token": {
                    "expires": null,
                    "id": "7db33cf3-b43b-4457-aaf7-ac7c7fae378e",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                }
            }

+ Response 401 (application/json)

        {
            "fields": {
                "email": [
                    "Invalid credentials"
                ],
                "password": [
                    "Invalid credentials"
                ]
            },
            "message": "Invalid credentials",
            "type": "invalid_auth"
        }

+ Response 400 (application/json)

        {
            "fields": {
                "passworad": [
                    "extra keys not allowed"
                ]
            },
            "message": "Validation Error",
            "type": "invalid_request_error"
        }

#### Get active tokens [/tokens]
Retrieve the list of tokens for my account
##### [GET]

+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "tokens": [
                {
                    "expires": null,
                        "id": "77e4717b-b475-46f2-862e-404f77419673",
                        "inherits_user_perms": true,
                        "permissions": [],
                        "roles": [],
                        "user_id": "22222222-1111-4111-8111-111111111111"
                },
                {
                    "expires": null,
                    "id": "29e5944f-e07e-4543-89b2-d1847b4f57d9",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                },
                {
                    "expires": null,
                    "id": "be3a1f67-4bf9-415a-a8bf-2f024d70e051",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                },
                {
                    "expires": null,
                    "id": "b8fcd81e-b015-4bfa-9a0e-53b71ef58f58",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                },
                {
                    "expires": "2014-02-04T12:14:33.950144+00:00",
                    "id": "09b36d4b-2842-48b4-acfa-62785bdfa3de",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": [],
                    "user_id": "22222222-1111-4111-8111-111111111111"
                }
            ]
        }

+ Response 401 (application/json)

        {
            "message": "This resource requires authentication but the header \"X-Auth-Token\" is missing.",
            "type": "invalid_auth"
        }

#### Get active token [/tokens/{token_id}]
Retrieve a specific tokens associate to my account
##### [GET]

+ Parameter

    + token_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Token unique identifier

+ Response 200 (application/json)

        {
            "token": {
                "expires": "2014-02-04T12:24:35.830623+00:00",
                "id": "09b36d4b-2842-48b4-acfa-62785bdfa3de",
                "inherits_user_perms": true,
                "permissions": [],
                "roles": [],
                "user_id": "22222222-1111-4111-8111-111111111111"
            }
        }

+ Response 404 (application/json)

        {
            "message": "Not found",
            "type": "unknown_resource"
        }

#### Get active token permissions [/tokens/{token_id}/permissions]
Retrieve permissions for a specific tokens associate to my account
##### [GET]

+ Parameter

    + token_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Token unique identifier

+ Response 200 (application/json)

        {
            "permissions": {
                "account": {
                    "organization:*": [
                        "22222222-1111-4111-8111-222222222222",
                        "11111111-1111-4111-8111-111111111111",
                        "",
                        ""
                    ],
                    "organization:read": [
                        "22222222-1111-4111-8111-222222222222",
                        "22222222-1111-4111-8111-222222222222",
                        "11111111-1111-4111-8111-111111111111",
                        "11111111-1111-4111-8111-111111111111"
                    ],
                    "token:*": [
                        "22222222-1111-4111-8111-111111111111"
                    ],
                    "user:*": [
                        "22222222-1111-4111-8111-111111111111",
                        ""
                    ],
                    "users:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        ""
                    ],
                    "users:read": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ]
                },
                "compute": {
                    "images:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        ""
                    ],
                    "images:read": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ],
                    "ips:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        ""
                    ],
                    "ips:read": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ],
                    "servers:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        ""
                    ],
                    "servers:read": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ],
                    "volumes:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        ""
                    ],
                    "volumes:read": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ]
                },
                "storage": {
                    "storage:*": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        "11111111-1111-4111-8111-111111111111:*",
                        ""
                    ],
                    "storage:read": [
                        "22222222-1111-4111-8111-222222222222:*",
                        "11111111-1111-4111-8111-111111111111:*"
                    ]
                },
                "ticket": {
                    "tickets:*": [
                        "22222222-1111-4111-8111-111111111111",
                        ""
                    ]
                }
            }
        }

+ Response 404 (application/json)

        {
            "message": "Not found",
                "type": "unknown_resource"
        }

#### Delete an active token [/tokens/{token_id}]
Delete a specific tokens associate to my account
##### [DELETE]

+ Parameter

    + token_id (required, string, `09b36d4b-2842-48b4-acfa-62785bdfa3de`)... Token unique identifier

+ Response 204

+ Response 400 (application/json)

        {
            "message": "Invalid UUID 09b36d4b-2842-48b4-acfa-62785bdfa3e",
            "type": "invalid_request_error"
        }

### group Users
Resources related to scaleway Users

#### Get user information [/users/{user_id}]
Retrieve information for the specified user
##### [GET]

+ Parameter

    + user_id (required, string, `22222222-1111-4111-8111-111111111111`)... User unique identifier

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
                        "name": "HyperScale"
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
                            "name": "HyperScale"
                        },
                        "role": "admin"
                    },
                    {
                        "organization": {
                            "id": "11111111-1111-4111-8111-111111111111",
                            "name": "HyperScale"
                        },
                        "role": "ocs_admin"
                    }
                ]
            }
        }

+ Response 404 (application/json)

        {
            "message": "User not found",
            "type": "unknown_resource"
        }

+ Response 401 (application/json)

        {
            "message": "Invalid authentication token: 77e4717b-b475-46f2-862e-404f77419672",
            "type": "invalid_auth"
        }

### group TODO
Not yet documented resources (internal)

#### Reset password [/reset_password]

#####[POST]

#####[PUT]


#### Create user [/users]

#####[POST]

#### User resources [/users/{user_id}]

#####[PUT] 

#####[PATCH]

#### Create role [/roles]

##### [POST]

#### Get user roles [/roles/{user_id}]

##### [GET]

#### Get organization roles [/roles/{organization_id}]

##### [GET]

#### S3 tokens [/s3compat/s3tokens]

##### [POST]

#### S3 users [/s3compat/users/{user_id}]

##### [GET]

#### S3 Credentials OS-EC2 [/s3compat/users/<user_id>/credentials/OS-EC2]

##### [GET]


