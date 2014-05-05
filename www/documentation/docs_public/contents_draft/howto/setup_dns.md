---
title: Set up your domains
template: article.jade
position: 3
---

We offer a simple and easy to use DNS manager for your domains.

This article will guide you through the process of managing your domains and how to use the DNS manager.

This guide assumes you've have the following :

- A registered domain name (e.g. myserver.com) using a domain registrar.
- An active instance, with a public IP address (e.g 1.2.3.4).

#### Step 1 - Change your Domain Name Server

The first thing you need to do to set up your domain is to change your Domain Name Server

From your registrar control panel, find the section called "Domain Name Server" or "DNS"

Change the nameserver to point on our, just fill namservers fields with the following.

- nsx.hyperscale.com
- nsx.hyperscale.com
- nsx.hyperscale.com
- nsx.hyperscale.com

And save your changes.

You can verify that new name servers are registered with `whois` command.

```
$whois yourdomain.com

Whois Server Version 2.0

Domain names in the .com and .net domains can now be registered
with many different competing registrars. Go to http://www.internic.net
for detailed information.

   Domain Name: yourdomain.com
   Name Server: nsx.hyperscale.com
   Name Server: nsx.hyperscale.com
   Name Server: nsx.hyperscale.com
   Updated Date: 21-jan-2014
   Creation Date: 29-apr-2011
   Expiration Date: 29-apr-2014
```

#### Step 2 - Domain configuration

Now we need move into the [console](https://console.cloud.online.net).

Within the DNS section, click "Create DNS zone", and fill domain name with your domain name ex: `mydomain.com`

![DNS](../imgs/img_tmp_dns.png "Temporaire")

You will reach a page where you can enter all of your domain details.

#### Step 3 - Entry types

- A records

Use this record to point a name on the IP address of an instance.

`test.mydomain.com A xxx.xxx.xxx.xxx`

- CNAME records

The CNAME record works as an alias of the A record.

`www.mydomain.com CNAME test.mydomain.com`

- MX records

The MX Records designate the order in which the mail servers should be attempted to be reached.

`mx1.mydomain.com 1`

`mx1.mydomain.com 5`

`mx1.mydomain.com 10`

#### Step 4 - Testing

Once you have configured your domains, you can test everything works fine. (It can take some time to be update)

Test via command line

```
$nslookup test.mydomain.com

Name: test.mydomain.com
Address: xxx.xxx.xxx.xxx
```


