FROM bde2020/spark-master:3.0.1-hadoop3.2

WORKDIR /root

ENV LANG="ja_JP.utf8" \
    LANGUAGE="ja_JP.utf8" \
    LC_ALL="ja_JP.utf8"

RUN apk --update add coreutils
RUN apk add procps

RUN rm -f /usr/bin/python \
    && ln -s /usr/bin/python3.7 /usr/bin/python \
    && pip3 install --upgrade pip

RUN mkdir /tmp/spark-events \
    && mkdir /usr/local/lib/jars

COPY files/etc /etc
COPY lib/jars /usr/local/lib/jars

RUN mv /etc/spark-defaults.conf /spark/conf
