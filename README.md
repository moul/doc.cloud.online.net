# doc.cloud.online.net

## Install dependencies
```
cd www
npm install
npm install -g grunt-cli aglio
bower install
```

## Edit public documentation (livereload)
```
cd www/utils/bin
node wintersmit_docs_public.js
browser : http://localhost:8080
```

## Edit api documentation (livereload)
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
