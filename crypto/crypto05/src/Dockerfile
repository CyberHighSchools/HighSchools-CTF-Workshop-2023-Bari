FROM nikolaik/python-nodejs:python3.10-nodejs19-alpine

ADD app /src
WORKDIR /src

RUN apk add --no-cache make g++
RUN npm install
RUN pip install mtp
RUN adduser -D ctf
USER ctf


EXPOSE 8080

CMD node backend.js