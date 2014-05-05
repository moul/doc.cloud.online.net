FORMAT: 1A

# Welcome to the API documentation.

We have created an easy to use and restfi; API that allows you to have a full control over the service. All feature you will find in the web control panel are also available through the API.

## Request and response

Our api works over https and is accessed from the `api.labs.online.net` domain. All data is sent and received as json.

## Constructing Requests

Requests are made of three components:

- Base URL: `https://api.labs.online.net`
- API version: `v1`
- Resource path: `users`

To construct a proper request, you will need to format the URL as follows:

`https://api.labs.online.net/{version}/{ressource}`

Example: `https://api.labs.online.net/v1/users/22222222-1111-4111-8111-111111111111`

An example request, to retrieves detailed informations about a user might be:

```
curl -i 'https://api.labs.online.net/v1/users/22222222-1111-4111-8111-111111111111' --header "X-Auth-Token: 59517bee-4ccb-43fa-95d0-f52292aad10a"

HTTP/1.0 200 OK
Content-Type: application/json

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
```

## Basic Authentication

You authenticate to the HyperScale API by requesting a token. A token is produce by requesting /tokens ressource via POST request.

Basic Authentication process:

- Query via POST request the /token ressource (see here how to)

- Supply an "X-Auth-Token" header followed by the token you get previously, e.g. "4e0b46e4-7c1d-44d4-8ba6-dc5f80694397"

```
curl -X GET -H "X-Auth-Token: 4e0b46e4-7c1d-44d4-8ba6-dc5f80694397" -H "Content-Type: application/json" https://api.labs.online.net/v1/{ressources}
```

## Errors

We use conventional HTTP response codes to indicate success or failure of an API request.

In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that resulted from the provided information (e.g. a required parameters were missing, etc.), and codes in the 5xx range indicate an error with our servers.

### HTTP Status Code Summary

- `200 OK` - Everything worked as expected.
- `400 Bad Request` - Often missing a required parameter.
- `401 Unauthorized` - No valid API key provided.
- `402 Request Failed` - Parameters were valid but request failed.
- `403 Forbidden` - Insufficient privileges to access requested resource.
- `404 Not Found` - The requested item doesn't exist.
- `50x` Server errors - something went wrong on HyperScale's end.

Input and output data must be valid JSON with appropriate Content-Type header set.

### Attributes

- type:
 
 - invalid_request_error: Occured when your request has an invalid parameters.
 - invitalid_auth: Arise when there is a problem of authentication.
 - uknown_resource: Occured when the resource doesn't exist.
 - authorization_required: You don't have sufficient right to access the resource.
 - api_error: API errors is used in case of problem with HyperScale's servers

- message:
 
 - A human readable error giving more details about the error

- fields (Optional):

 - An array of parameters with an human readable message giving more details about the error.

### Errors responses example 

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

+ Response 401 (application/json)
        {
            "message": "The header 'X-Auth-Token' is missing",
            "type": "invalid_auth"
        }

+ Response 403 (application/json)
        {
          "message": "The token provided doesn't have the requested permission.",
          "type": "authorization_required"
        }

+ Response 404 (application/json)
        {
            "message": "User not found",
            "type": "unknown_resource"
        }

### Pagination (OUTDATED)

Methods returning multiple items are paginated to 25 items by default.
You can specify further pages with the ?page parameter. You can also set a custom page size up to 500 with the ?page_size parameter.

```
$curl -i https://api.hyperscale.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=5&page_size=150

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Status: 200 OK
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
X-RateLimit-Reset: 1389359739
Link: <https://api.hyperscale.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=1&page_size=150>; rel="first", <https://api.hyperscale.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=4&limit=150>; rel="prev", <https://api.hyperscale.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=6&limit=150>; rel="next", <https://api.hyperscale.com/v1/servers/Server-198779b8-e4b5-4876-9e2f-aa09c1ce9ebf/tags?page=10&limit=150>; rel="last",

...
```

## Resources

