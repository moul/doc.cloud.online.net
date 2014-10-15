---
title: How to use the API
template: article.jade
position: 6
---

This page shows you some basics to interact with our Compute API.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have configured your [SSH Key](/howto/ssh_keys.html)
- You have generated your [API Token](/howto/credentials.html)
- You know your [Organization ID](/advanced/api_organization.html)

There are five steps to provision and start a server with additional volume from the API. In this section, we will:

- [Retrieve the list of images available](/advanced/api.html#step-1-retrieve-the-list-of-images-available)
- [Create a new server](/advanced/api.html#step-2-create-a-new-server)
- [Create a new volume](/advanced/api.html#step-3-create-a-new-volume)
- [Attach the volume to the server](/advanced/api.html#step-4-attach-the-volume-to-the-server)
- [Start a server](/advanced/api.html#step-5-start-a-server)

#### Step 1 - Retrieve the list of images available

The following request returns the list of available images. In this example we only have one image which is named `Ubuntu Trusty (14.04) on SSD 2014.06.04` and has id `fe8dfea7-bb8c-490c-a554-1a44a3c4af8c`.

Request
```
curl -H "X-Auth-Token: <YOUR_API_TOKEN_HERE>" https://api.cloud.online.net/images
```
Response
```
{
  "images": [
    {
      "arch": "arm",
      "creation_date": "2014-06-04T12:38:32.534063+00:00",
      "extra_volumes": "[]",
      "from_image": null,
      "from_server": null,
->    "id": "fe8dfea7-bb8c-490c-a554-1a44a3c4af8c", 
      "marketplace_key": null,
      "modification_date": "2014-06-04T12:38:32.534063+00:00",
->    "name": "Ubuntu Trusty (14.04) on SSD 2014.06.04",
      "organization": "cc57d96c-03ac-44a5-bc91-8d1de2bbf8a8",
      "public": true,
      "root_volume": {
        "id": "c583bf78-ebd5-4ebc-863f-71905d2c39fd",
        "name": "Ubuntu Trusty RootFS snapshot"
      }
    }
  ]
}
```

#### Step 2 - Create a new server

To create a server, you have to fill out the following input:

- A server name
- An [Organization ID](/advanced/api_organization.html)
- An [Image ID](/advanced/api.html#step-1-retrieve-the-list-of-images-available)
- Tags (Optional)

Request
```
curl https://api.cloud.online.net/servers \
-H "X-Auth-Token: <YOUR_API_TOKEN_HERE>" \
-H "Content-Type: application/json" \
-d '{ \
"name": "<YOUR_SERVER_NAME>",
"image": "fe8dfea7-bb8c-490c-a554-1a44a3c4af8c",
"tags": ["temporary", "test"],
"organization": "<YOUR_ORGANIZATION_ID>"
}'
```
Response
```
{
  "server": {
    "dynamic_public_ip": false,
    "id": "c88d1aee-b65d-4ab9-bafd-3df293782693",
    "image": {
      "id": "fe8dfea7-bb8c-490c-a554-1a44a3c4af8c",
      "name": "Ubuntu Trusty (14.04) on SSD 2014.06.04"
    },
    "name": "<YOUR_SERVER_NAME>",
    "organization": "<YOUR_ORGANIZATION_ID>",
    "private_ip": null,
    "public_ip": null,
    "state": "stopped",
    "state_detail": "",
    "tags": [
      "temporary",
      "test"
    ],
    "volumes": {
      "0": {
        "export_uri": null,
        "id": "1a96f139-95f8-4680-aeeb-0a58229d18d5",
        "name": "Ubuntu Trusty RootFS snapshot",
        "organization": "<YOUR_ORGANIZATION_ID>",
        "server": {
          "id": "c88d1aee-b65d-4ab9-bafd-3df293782693",
          "name": "<YOUR_SERVER_NAME>"
        },
        "size": 20000000000,
        "volume_type": "l_ssd"
      }
    }
  }
}
```

The response above returns an HTTP 201 code with the server details.

#### Step 3 - Create a new volume

To create a volume, you have to fill out the following input:

- A volume name
- An [Organization ID](/advanced/api_organization.html)
- A size in GB
- The volume type - LSSD (Local solid state drive) or LHDD (Local spinning disk)

You can create and attach additional volumes to an existing server.
The server must be stopped.

Let's create a new volume of type SSD with a size of 10GB.

Request
```
curl https://api.cloud.online.net/volumes \
-H "X-Auth-Token: <YOUR_API_TOKEN_HERE>" \
-H "Content-Type: application/json" \
-d '{
"name": "<YOUR_VOLUME_NAME>",
"organization": "<YOUR_ORGANIZATION_ID>",
"size": 10000000000,
"volume_type": "l_ssd"
}'
```
Response
```
{
  "volume": {
    "export_uri": null,
    "id": "65e7d766-103b-4fb1-819a-fb95e3a15348",
    "name": "<YOUR_VOLUME_NAME>",
    "organization": "<YOUR_ORGANIZATION_ID>",
    "server": null,
    "size": 10000000000,
    "volume_type": "l_ssd"
  }
}
```

The response above returns an HTTP 201 code with the volume details.

#### Step 4 - Attach the volume to the server

To attach an additional volume to an existing server, you have to perform a PUT method requests on the server.


Request
```
curl https://api.cloud.online.net/servers/<YOUR_SERVER_ID> \
-H "X-Auth-Token: <YOUR_API_TOKEN_HERE>" \
-H "Content-Type: application/json" \
-X PUT
-d '{
"dynamic_public_ip": false,
"id": "c88d1aee-b65d-4ab9-bafd-3df293782693",
"image": {
"id": "fe8dfea7-bb8c-490c-a554-1a44a3c4af8c",
"name": "Ubuntu Trusty (14.04) on SSD 2014.06.04"
},
"name": "<YOUR_SERVER_NAME>",
"organization": "<YOUR_ORGANIZATION_ID>",
"private_ip": null,
"public_ip": null,
"state": "stopped",
"state_detail": "",
"tags": [
"temporary",
"test"
],
"volumes": {
---> "0": {"id": "1a96f139-95f8-4680-aeeb-0a58229d18d5", "name": "volume 1"},
---> "1": {"id": "65e7d766-103b-4fb1-819a-fb95e3a15348", "name": "volume 2"}
}
}'
```
Response
```
{
  "server": {
    "dynamic_public_ip": false,
    "id": "c88d1aee-b65d-4ab9-bafd-3df293782693",
    "image": {
      "id": "fe8dfea7-bb8c-490c-a554-1a44a3c4af8c",
      "name": "Ubuntu Trusty (14.04) on SSD 2014.06.04"
    },
    "name": "<YOUR_SERVER_NAME>",
    "organization": "<YOUR_ORGANIZATION_ID>",
    "private_ip": null,
    "public_ip": null,
    "state": "stopped",
    "state_detail": "",
    "tags": [
      "temporary",
      "test"
    ],
    "volumes": {
      "0": {
        "export_uri": null,
        "id": "1a96f139-95f8-4680-aeeb-0a58229d18d5",
        "name": "Ubuntu Trusty RootFS snapshot",
        "organization": "<YOUR_ORGANIZATION_ID>",
        "server": {
          "id": "c88d1aee-b65d-4ab9-bafd-3df293782693",
          "name": "<YOUR_SERVER_NAME>"
        },
        "size": 20000000000,
        "volume_type": "l_ssd"
      },
      "1": {
        "export_uri": null,
        "id": "65e7d766-103b-4fb1-819a-fb95e3a15348",
        "name": "<YOUR_VOLUME_NAME>",
        "organization": "<YOUR_ORGANIZATION_ID>",
        "server": {
          "id": "c88d1aee-b65d-4ab9-bafd-3df293782693",
          "name": "<YOUR_SERVER_NAME>"
        },
        "size": 10000000000,
        "volume_type": "l_ssd"
      }
    }
  }
}
```

#### Step 5 - Start a server

To start your server, execute the following request where `<YOUR_SERVER_ID>` is your server id.

Request
```
 curl -H "X-Auth-Token: <YOUR_API_TOKEN_HERE>" https://api.cloud.online.net/servers/<YOUR_SERVER_ID>/action \
 -d '{"action":"poweron"}' -H "Content-Type: application/json"
```
Response
```
{
  "task": {
    "description": "server_batch_poweron",
    "href_from": "/servers/c88d1aee-b65d-4ab9-bafd-3df293782693/action",
    "id": "1f8e2202-83b3-463b-948d-9d1e5aa7dfe1",
    "progress": "0",
    "started_at": "2014-07-22T12:17:39.067932+00:00",
    "status": "pending",
    "terminated_at": null
  }
}
```

To go even further you can access the [API Documentation](/api/).
