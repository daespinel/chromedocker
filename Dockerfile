FROM jess/chrome:latest
MAINTAINER David Espinel <dafespinelsa@unal.edu.co>
RUN \
  apt-get update && apt-get purge openssh-client && apt-get install openssh-client -y && \
  apt-get install python -y


WORKDIR /data
CMD service ssh start && /bin/sh
EXPOSE 5901
EXPOSE 22
