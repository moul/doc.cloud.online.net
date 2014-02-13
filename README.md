# Documentation

## Install
```
cd scaleway
npm install
npm install -g grunt-cli aglio
```

##edit internal documentation (liverealod)
```
cd scaleway/utils/bin
node wintersmit_docs_internal.js
browser : http://localhost:8080
```

##edit public documentation (livereload)
```
cd scaleway/utils/bin
node wintersmit_docs_public.js
browser : http://localhost:8080
```

##edit api documentation (livereload)
```
cd documentation/api
aglio -i <input-file>.md -s
browser : http://localhost:3000
```


## Generate static files for deployment
```
grunt
```

- API static files are in dist/api

- Public documentation static files are in dist/docs_public/

- Internal documentation static files are in dist/docs_internal/


