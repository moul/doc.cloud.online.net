FORMAT: 1A

# Welcome to cloud.online.net API documentation.

We have created an easy to use and RESTful API that allows you to have a full control over the service. All feature you will find in the web control panel are also available through the API.

## Request and response

Our api works over https and is accessed from two endpoint:

- `account.cloud.online.net` domain for account actions
- `api.cloud.online.net` domain for compute actions

All data is sent and received as json.

## Constructing Requests

Requests are made of two components:

- Base URL: `https://api.cloud.online.net`
- Resource path: `servers`

To construct a proper request, you will need to format the URL as follows:

`https://api.cloud.online.net/{ressource}`

Example: `https://api.cloud.online.net/servers/49016330-e07b-4d54-ba0d-6f0b67ab3d6d`

An example request, to retrieves detailed informations about a server might be:

```
% curl -H 'X-Auth-Token: 017ce0ce-20ec-4d4ez-b44c-e561a4421d2c' -H 'Content-Type: application/json' https://api.cloud.online.net/servers -i

HTTP/1.1 200 OK
Server: nginx
Date: Thu, 22 May 2014 07:55:00 GMT
Content-Type: application/json
Content-Length: 1345
Connection: keep-alive
X-Sentry-ID: None
Strict-Transport-Security: max-age=86400

{
  "servers": [
    {
      "dynamic_public_ip": false,
      "id": "5a84cfd1-ba2a-4576-b55c-f11dcdd7059f",
      "image": {
        "id": "85917034-46b0-4cc5-8b48-f0a2245e357e",
        "name": "ubuntu working"
      },
      "name": "My first server",
      "organization": "ecc1c86a-eabb-43a7-9c0a-77e371753c0a",
      "private_ip": null,
      "public_ip": null,
      "running": false,
      "tags": [
        "firstserver",
        "new"
      ],
      "volumes": {
        "0": {
          "export_uri": null,
          "id": "0731e0c0-6931-4b99-a8f9-c593b4f3d8c1",
          "name": "vol simple snapshot",
          "organization": "ecc1c86a-eabb-43a7-9c0a-77e371753c0a",
          "server": {
            "id": "5a84cfd1-ba2a-4576-b55c-f11dcdd7059f",
            "name": "My first server"
          },
          "size": 10000000000,
          "volume_type": "l_hdd"
        },
        "1": {
          "export_uri": null,
          "id": "cc0bbb40-7a08-4bf3-a6d9-68b0ffb1ef0e",
          "name": "default_volume_name",
          "organization": "ecc1c86a-eabb-43a7-9c0a-77e371753c0a",
          "server": {
            "id": "5a84cfd1-ba2a-4576-b55c-f11dcdd7059f",
            "name": "My first server"
          },
          "size": 10000000000,
          "volume_type": "l_ssd"
        }
      }
    }
  ]
}
```

## Basic Authentication

You authenticate to the API by requesting a token. A token is produce by requesting /tokens ressource via POST request.

Basic Authentication process:

- Query via POST request the /tokens ressource [see here how to](/#page:tokens,header:tokens-tokens-collection-post)

- Supply an "X-Auth-Token" header followed by the token you get previously, e.g. "4e0b46e4-7c1d-44d4-8ba6-dc5f80694397"

```
curl -X GET -H "X-Auth-Token: 4e0b46e4-7c1d-44d4-8ba6-dc5f80694397" -H "Content-Type: application/json" https://api.cloud.online.net/{ressources}
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
- `50x` Server errors - something went wrong on api.cloud.net's end.

Input and output data must be valid JSON with appropriate Content-Type header set.

### Attributes

- type:
 
 - invalid_request_error: Occured when your request has an invalid parameters.
 - invitalid_auth: Arise when there is a problem of authentication.
 - uknown_resource: Occured when the resource doesn't exist.
 - authorization_required: You don't have sufficient right to access the resource.
 - api_error: API errors is used in case of problem with api.cloud.online's servers

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


