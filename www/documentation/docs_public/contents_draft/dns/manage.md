---
title: Manage
template: article.jade
position: 3 
---

In the previous article you learned how to identify our nameservers, and that you will have to update them with your current domain registrar in order to transfer an existing domain to be served from our service. 

Managing and Creating DNS records for your domains is easy to do within the [console](https://console.cloud.online.net).
. 

In this article, we will look at creating a DNS zone for your domain and adding basic A, MX, and CNAME records using the service.


#### Step 1 - Create DNS zone

Within the DNS section, click "Create DNS zone", and fill domain name with your domain name ex: `mydomain.com`

![DNS](../imgs/img_tmp_dns.png "Temporaire")

You will reach a page where you can enter some records.

#### Step 2 - Entry types

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

#### Step 43- Testing

Once you have configured your domains, you can test everything works fine. (It can take some time to be update)

Test via command line

```
$nslookup test.mydomain.com

Name: test.mydomain.com
Address: xxx.xxx.xxx.xxx
```
