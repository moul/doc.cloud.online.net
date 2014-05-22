### group Tokens

This resources of API methods allows you to create, manage or delete your tokens

#### Tokens Collection [/tokens]

A collection of tokens with all their details

##### Create a token [POST]

Create a new token for the specified user

+ Parameters
    + email (required, string, `jsnow@got.com`)... User email
    + password (required, string, `winteriscoming`)... User password
    + expires (optional, boolean, `false`)... Set if you want a token wich doesn't expire (default: true)

+ Request (application/json)

    + Body

            {
                "email": "jsnow@got.com",
                "password": "winteriscoming",
                "expires": false
            }

+ Response 201

    + Headers (application/json)
           
            location: https://account.cloud.online.net/tokens/9de8f869-c58e-4aa3-9208-2d4eaff5fa20

    + Body

            {
                "token": {
                    "creation_date": "2014-05-22T08:05:57.556385+00:00",
                    "expires": null,
                    "id": "9de8f869-c58e-4aa3-9208-2d4eaff5fa20",
                    "inherits_user_perms": true,
                    "permissions": [],
                    "roles": {
                      "organization": null,
                      "role": null
                    },
                    "user_id": "5bea0358-db40-429e-bd82-914686a7e7b9"
                }
            }

##### List all Tokens [GET]

Retrieve a list of Tokens with all their details

+ Response 200 (application/json)

        {
            {
                "tokens": [
                    {
                        "creation_date": "2014-03-13T10:53:11.456319+00:00",
                        "expires": null,
                        "id": "4e5570fb-c854-5349-979f-9f51d608d34z",
                        "inherits_user_perms": true,
                        "permissions": [],
                        "roles": {
                            "organization": null,
                            "role": null
                        },
                        "user_id": "5bea0358-db40-429e-bd82-953016a7e2s7"
                    },
                   {
                        "creation_date": "2014-05-19T18:05:47.304433+00:00",
                        "expires": "2014-05-20T14:05:06.393875+00:00",
                        "id": "654c95b0-2cf5-41a3-b3cc-733ffba4b4b7",
                        "inherits_user_perms": true,
                        "permissions": [],
                        "roles": {
                            "organization": null,
                            "role": null
                        },
                        "user_id": "5bea0358-db40-429e-bd82-953016a7e2s7"
                    }
                ]
            }
        }


#### Token [/tokens/{token_id}]

A single token with all its details

+ Parameters
    + token_id (required, string, `654c95b0-2cf5-41a3-b3cc-733ffba4b4b7`)... Token unique identifier

##### Retrieve a token [GET]

Retrieve details about a token

+ Response 200 (application/json)

        {
            "token": {
                "creation_date": "2014-05-22T08:06:51.742826+00:00",
                "expires": "2014-05-20T14:05:06.393875+00:00",
                "id": "654c95b0-2cf5-41a3-b3cc-733ffba4b4b7",
                "inherits_user_perms": true,
                "permissions": [],
                "roles": {
                    "organization": null,
                    "role": null
                },
                "user_id": "5bea0358-db40-429e-bd82-953016a7e2s7"
            }
        }


##### Update token [PATCH]

Increase token expiration time of 30 minutes

+ Response 200 (application/json)

        {
            "token": {
                creation_date": "2014-05-22T08:06:51.742826+00:00",
                "expires": "2014-05-22T11:18:07.786841+00:00",
                "id": "654c95b0-2cf5-41a3-b3cc-733ffba4b4b7",
                "inherits_user_perms": true,
                "permissions": [],
                "roles": {
                    "organization": null,
                    "role": null
                },
                "user_id": "5bea0358-db40-429e-bd82-953016a7e2s7"
            }
        }



##### Remove a token [DELETE]

+ Response 204


### group Users

Resources related to Users

#### User [/users/{user_id}]

Retrieve informations for the specified user

+ Parameter
    + user_id (required, string, `5bea0358-db40-429e-bd82-953016a7e2s7`)... User unique identifier

##### Retrieve a user [GET]

Retrieve details about a user


+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)


            "user": {
                "email": "jsnow@got.com",
                "firstname": "John",
                "fullname": "Jhon Snow",
                "id": "5bea0358-db40-429e-bd82-953016a7e2s7",
                "lastname": "Snow",
                "organizations": null,
                "roles": null,
                "ssh_public_keys": null
            }




