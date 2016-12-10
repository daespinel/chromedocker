FROM chrisdaish/google-chrome
MAINTAINER David Espinel <dafespinelsa@unal.edu.co>

RUN \
  apt-get update && apt-get purge openssh-client && apt-get install openssh-client -y && \
  apt-get install python -y && apt-get install -y net-tools

#COPY hosts /etc/

COPY hosts.sh /home/
RUN	sudo chmod +x /home/hosts.sh

WORKDIR /home

EXPOSE 5901
EXPOSE 22

RUN /home/hosts.sh

ENTRYPOINT ["sh", "-c", "/home/hosts.sh ; /usr/local/bin/start-google-chrome.sh"]

#CMD /bin/sh \
#	&& echo '192.168.0.1 page1.com' >> /etc/hosts \
#	&& echo '192.168.0.2 page2.com' >> /etc/hosts \
#	&& echo '192.168.0.3 page3.com' >> /etc/hosts \
#	&& echo '192.168.0.4 page4.com' >> /etc/hosts \

