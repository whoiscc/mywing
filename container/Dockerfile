FROM tiangolo/uwsgi-nginx:python3.7-alpine3.9

LABEL maintainer="FinnTenzor <finntenzor@gmail.com>"

COPY ./whls /tmp/whls/
COPY ./build.sh /tmp/build.sh

RUN /bin/sh /tmp/build.sh \
    && rm /tmp/build.sh
