# Online Labs documentation

[![GuardRails badge](https://badges.production.guardrails.io/moul/doc.cloud.online.net.svg)](https://www.guardrails.io)

This repository contains the source for Online Labs documentation.

- Documentation files are [here](https://github.com/online-labs/doc.cloud.online.net/tree/master/www/documentation/docs_public/contents) and use Markdown.
- API Documentation files are [here](https://github.com/online-labs/doc.cloud.online.net/tree/master/www/documentation/api/content) and use [API Blueprint](https://github.com/apiaryio/api-blueprint).

## Getting started

### Install dependencies
```
cd www
npm install
npm install -g grunt-cli aglio
bower install
```

### Edit public documentation (livereload)
```
cd www/utils/bin
node wintersmit_docs_public.js
browser : http://localhost:8080
```

### Edit api documentation (livereload)
```
cd www/documentation/api
aglio -i <input-file>.md -s
browser : http://localhost:3000
```

## Docker

Run:

`docker run -it --rm -p 8080:8080 onlinelabs/doc.cloud.online.net`

Build:

`docker build -t onlinelabs/doc.cloud.online.net .`

