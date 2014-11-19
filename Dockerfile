FROM node:latest
MAINTAINER Manfred Touron <mtouron@ocs.online.net>

# Install dependencies
RUN mkdir /www
WORKDIR /www

RUN npm install -g grunt-cli aglio bower
ADD www/package.json /www/package.json
RUN npm install

ADD www/bower.json /www/bower.json
ADD www/.bowerrc /www/.bowerrc
RUN bower --allow-root install

# Add code
ADD www /www

## Edit public documentation (livereload)
CMD ["bash", "-c", "cd utils/bin && node wintersmit_docs_public.js"]
EXPOSE 8080
