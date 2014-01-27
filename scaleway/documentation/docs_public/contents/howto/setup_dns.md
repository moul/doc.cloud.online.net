---
title: Set up your domains with Scaleway
template: article.jade
---

##Intro

Scaleway offer a simple, easy to use DNS manager for your domains.

This guide gonna show you how to manage your domains with Scaleway & how to use Scaleway DNS manager.

##Step 1 - Change your Domain Name Server

The first thing you need to do to set up your domain is to set your Domain Name Server to point to Scaleway DNS.

From your registrar control panel, find the section called "Domain Name Server" or "DNS"

Change the nameserver to point on Scaleway name server, just fill namservers fields with the following.

- nsx.scaleway.com
- nsx.scaleway.com
- nsx.scaleway.com
- nsx.scaleway.com

Once done, save your changes.

You can verify that new name servers are registered with `whois` command.

```
$whois yourdomain.com

Whois Server Version 2.0

Domain names in the .com and .net domains can now be registered
with many different competing registrars. Go to http://www.internic.net
for detailed information.

   Domain Name: yourdomain.com
   Name Server: nsx.scaleway.com
   Name Server: nsx.scaleway.com
   Name Server: nsx.scaleway.com
   Updated Date: 21-jan-2014
   Creation Date: 29-apr-2011
   Expiration Date: 29-apr-2014
```

##Step 2 - Domain configuration

First go to the [Scaleway Dashboard](xxx).

From the menu, move to DNS Section and click "Create DNS zone" fill domain name with your domain name ex: `mydomain.com`.

You will reach a page where you can enter all of your domain details.

##Step 3 - Entry types

- A records

Use this record to point a name on the IP address of a Scaleway instance for example.

`test.mydomain.com A xxx.xxx.xxx.xxx`

- CNAME records

The CNAME record works as an alias of the A record.

`www.mydomain.com CNAME test.mydomain.com`

- MX records

The MX Records designate the order in which the mail servers should be attempted to be reached.

`mx1.mydomain.com 1`

`mx1.mydomain.com 5`

`mx1.mydomain.com 10`

##Step 4 - Testing

Once you have configured your domains, you can test everything works fine. (It can take some time to be update)

Test via command line

```
$nslookup test.mydomain.com

Name: test.mydomain.com
Address: xxx.xxx.xxx.xxx
```


