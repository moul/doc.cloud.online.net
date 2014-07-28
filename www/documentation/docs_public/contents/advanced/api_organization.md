---
title: Retrieve your organization ID
template: article.jade
position: 5
---

This page shows you how to identify your organization ID through the API.

> <strong>Requirements</strong>
- You have an account and are logged into [cloud.online.net](//cloud.online.net)
- You have generated a [token](/account/credentials.html)

Our system attributes an organization ID to each user.<br/>
The API requires your organization ID for many actions, for instance:

- Server creation
- Volume creation
- Image creation
- Snapshot creation
- Etc.


### Retrieve your organization ID

To retrieve your organization ID, execute the following request.

N.B. Replace the `X-Auth-Token` value with your generated token

```
% curl https://account.cloud.online.net/organizations -H "X-Auth-Token: fa633f07-c2e9-4f06-b651-011d5330e58f"

{
  "organizations": [
    {
->    "id": "000a115d-2852-4b0a-9ce8-47f1134ba95a",
      "name": "john.snow@xxxx.x",
      "users": [
        {
          ...
        }
      ]
    }
  ]
}
```

In the above example, the organization ID is `000a115d-2852-4b0a-9ce8-47f1134ba95a`

