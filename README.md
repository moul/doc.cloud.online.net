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

## Generate static files for deployment
```
grunt
```

- API static files are in dist/api

- Public documentation static files are in dist/docs_public/
