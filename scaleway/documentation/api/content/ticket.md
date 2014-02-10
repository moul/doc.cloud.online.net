### group Ticket
Resources related to scaleway Ticket

#### Ticket creation [/ticket]
Create a new ticket
##### [POST]

+ Parameters

    + subject (required, string, `This is a new ticket`)... Ticket subject
    + answers (required, array, `[ {"content": "this is an answer"} ]`)... An array of answer(s)
    + tags (optional, array, `["this", "is", "a", "new", "ticket"]`)... Array of tags

+ Request (application/json)

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

    + Body

            {
                "subject": "This is a new ticket",
                "answers": [
                    {"content": "this is an answer"}
                ]
                "tags": ["this", "is", "a", "new", "ticket"]
            }

+ Response 201 (application/json)

        {
            "ticket": {
                "assigned_at": null,
                "assigned_by": null,
                "assigned_to": [],
                "closed_at": null,
                "created_at": "2014-02-10T14:32:02.741876+00:00",
                "created_by": {
                    "firstname": "Paul",
                    "fullname": "Paul Rodriguez",
                    "id": "22222222-1111-4111-8111-111111111111",
                    "lastname": "Rodriguez"
                },
                "finish_at": null,
                "id": "4ebcbb12-db00-452a-8858-0752dbd10fa6",
                "queue": "AUTH",
                "resolved": "False",
                "start_at": null,
                "state": "OPEN",
                "subject": "This a new ticket",
                "tags": [
                    {
                        "name": "this"
                    },
                    {
                        "name": "is"
                    },
                    {
                        "name": "a"
                    },
                    {
                        "name": "ticket"
                    }
                ],
                "updated_at": "2014-02-10T14:32:02.741888+00:00"
            }
        }

+ Response 400 (application/json)

        {
            "fields": {
                "subject": [
                    "required key not provided"
                ]
            },
            "message": "Validation Error",
            "type": "invalid_request_error"
        }

+ Response 401 (application/json)

        {
            "message": "Authentication error",
            "type": "invalid_auth"
        }

#### List all tickets [/ticket]
Retrieve a list of tickets
##### [GET]

+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "tickets": [
                {
                    "assigned_at": null,
                    "assigned_by": null,
                    "assigned_to": [],
                    "closed_at": null,
                    "created_at": "2014-02-10T14:37:15+00:00",
                    "created_by": {
                        "firstname": "Paul",
                        "fullname": "Paul Rodriguez",
                        "id": "22222222-1111-4111-8111-111111111111",
                        "lastname": "Rodriguez"
                    },
                    "finish_at": null,
                    "id": "7a9aca8d-69be-4ef3-957c-b19ab403b0c4",
                    "queue": "AUTH",
                    "resolved": "False",
                    "start_at": null,
                    "state": "OPEN",
                    "subject": "This a new ticket",
                    "tags": [
                        {
                            "name": "this"
                        },
                        {
                            "name": "is"
                        },
                        {
                            "name": "a"
                        },
                        {
                            "name": "new"
                        },
                        {
                            "name": "ticket"
                        }
                    ],
                    "updated_at": "2014-02-10T14:37:15+00:00"
                },
                {
                    "assigned_at": null,
                    "assigned_by": null,
                    "assigned_to": [],
                    "closed_at": null,
                    "created_at": "2014-02-10T14:37:34+00:00",
                    "created_by": {
                        "firstname": "Paul",
                        "fullname": "Paul Rodriguez",
                        "id": "22222222-1111-4111-8111-111111111111",
                        "lastname": "Rodriguez"
                    },
                    "finish_at": null,
                    "id": "9c1557fb-83b5-47f0-8ee5-73d48bd6dd96",
                    "queue": "AUTH",
                    "resolved": "False",
                    "start_at": null,
                    "state": "OPEN",
                    "subject": "This another ticket",
                    "tags": [
                        {
                            "name": "this"
                        },
                        {
                            "name": "is"
                        },
                        {
                            "name": "another"
                        },
                        {
                            "name": "ticket"
                        }
                    ],
                    "updated_at": "2014-02-10T14:37:34+00:00"
                }
            ]
        }

+ Response 401 (application/json)

        {
            "message": "Authentication error",
            "type": "invalid_auth"
        }

#### Get an existing ticket [/ticket/{ticket_id}]
Retrieve informations of an existing tickets
##### [GET]

+ Parameters
    
    + ticket_id (required, string, `afdca632-3d3e-4ddc-9fc3-3ad29af01c6c`)... Ticket unique identifier

+ Request

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

+ Response 200 (application/json)

        {
            "tickets": {
                "assigned_at": null,
                "assigned_by": null,
                "assigned_to": [],
                "closed_at": null,
                "created_at": "2014-02-10T14:44:12+00:00",
                "created_by": {
                    "firstname": "Paul",
                    "fullname": "Paul Rodriguez",
                    "id": "22222222-1111-4111-8111-111111111111",
                    "lastname": "Rodriguez"
                },
                "finish_at": null,
                "id": "afdca632-3d3e-4ddc-9fc3-3ad29af01c6c",
                "queue": "AUTH",
                "resolved": "False",
                "start_at": null,
                "state": "OPEN",
                "subject": "This is another ticket",
                "tags": [
                    {
                        "name": "this"
                    },
                    {
                        "name": "is"
                    },
                    {
                        "name": "another"
                    },
                    {
                        "name": "ticket"
                    }
                ],
                "updated_at": "2014-02-10T14:44:12+00:00"
            }
        }

+ Response 404 (application/json)

        {
            "message": "Not found",
            "type": "unknown_resource"
        }

+ Response 401 (application/json)

        {
            "message": "Authentication error",
            "type": "invalid_auth"
        }

#### Update an existing ticket [/ticket/{ticket_id}]
Change state of an existing tickets
##### [PATCH]

+ Parameters

    + ticket_id (required, string, `afdca632-3d3e-4ddc-9fc3-3ad29af01c6c`)... Ticket unique identifier
    + state (optional, string `CLOSE`)... Ticket state OPEN or CLOSE

+ Request (application/json)

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

    + Body

            {
                "state": "CLOSE"
            }

+ Response 200 (application/json)


        {
            "tickets": {
                "assigned_at": null,
                "assigned_by": null,
                "assigned_to": [],
                "closed_at": "2014-02-10T15:03:35+00:00",
                "created_at": "2014-02-10T14:44:12+00:00",
                "created_by": {
                    "firstname": "Paul",
                    "fullname": "Paul Rodriguez",
                    "id": "22222222-1111-4111-8111-111111111111",
                    "lastname": "Rodriguez"
                },
                "finish_at": null,
                "id": "afdca632-3d3e-4ddc-9fc3-3ad29af01c6c",
                "queue": "AUTH",
                "resolved": "False",
                "start_at": null,
                "state": "CLOSE",
                "subject": "This is another ticket",
                "tags": [
                    {
                        "name": "this"
                    },
                    {
                        "name": "is"
                    },
                    {
                        "name": "another"
                    },
                    {
                        "name": "ticket"
                    }
                ],
                "updated_at": "2014-02-10T15:03:35+00:00"
            }
        }

+ Response 400 (application/json)

        {
            "fields": {
                "xxx": [
                    "extra keys not allowed"
                ]
            },
            "message": "Validation Error",
            "type": "invalid_request_error"
        }

+ Response 404 (application/json)

        {
            "message": "Not found",
            "type": "unknown_resource"
        }

+ Response 401 (application/json)

        {
            "message": "Authentication error",
            "type": "invalid_auth"
        }

### Ticket response creation [/ticket/{ticket_id}/answers]
Create a new response to an existing ticket
##### [POST]

+ Parameters

    + ticket_id (required, string, `afdca632-3d3e-4ddc-9fc3-3ad29af01c6c`)... Ticket unique identifier
    + content (required, string, `This a ticket answer`)... Ticket response

+ Request (application/json)

    + Headers

            X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a

    + Body

            {
                "content": "This is another ticket response"
            }

+ Response 201 (application/json)

        {
            "answer": {
                "closed_at": null,
                "content": "This is another ticket response",
                "created_at": "2014-02-10T15:12:38.017896+00:00",
                "read_at": null,
                "sender": {
                    "firstname": "Paul",
                    "fullname": "Paul Rodriguez",
                    "id": "22222222-1111-4111-8111-111111111111",
                    "lastname": "Rodriguez"
                },
                "type": "web"
            }
        }

+ Response 400 (application/json)

        {
            "fields": {
                "xxx": [
                    "extra keys not allowed"
                ]
            },
            "message": "Validation Error",
            "type": "invalid_request_error"
        }

+ Response 404 (application/json)

        {
            "message": "Not found",
            "type": "unknown_resource"
        }

+ Response 401 (application/json)

        {
            "message": "Authentication error",
            "type": "invalid_auth"
        }

### Get ticket response creation [/ticket/{ticket_id}/answers]
Retrieve a list of responses for an existing ticket
##### [GET]

+ Parameters

    + ticket_id (required, string, `afdca632-3d3e-4ddc-9fc3-3ad29af01c6c`)... Ticket unique identifier

+ Response 200 (application/json)

        {
            "answers": [
                {
                    "closed_at": null,
                    "content": "This is a ticket response",
                    "created_at": "2014-02-10T15:11:46+00:00",
                    "read_at": null,
                    "sender": {
                        "firstname": "Paul",
                        "fullname": "Paul Rodriguez",
                        "id": "22222222-1111-4111-8111-111111111111",
                        "lastname": "Rodriguez"
                    },
                    "type": "web"
                },
                {
                    "closed_at": null,
                    "content": "This is another ticket response",
                    "created_at": "2014-02-10T15:12:38+00:00",
                    "read_at": null,
                    "sender": {
                        "firstname": "Paul",
                        "fullname": "Paul Rodriguez",
                        "id": "22222222-1111-4111-8111-111111111111",
                        "lastname": "Rodriguez"
                    },
                    "type": "web"
                }
            ]
        }

+ Response 404 (application/json)

        {
            "message": "Not found",
            "type": "unknown_resource"
        }

+ Response 401 (application/json)

        {
            "message": "Authentication error",
            "type": "invalid_auth"
        }
