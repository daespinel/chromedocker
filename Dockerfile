FROM chrisdaish/google-chrome
MAINTAINER David Espinel <dafespinelsa@unal.edu.co>

RUN \
  apt-get update && apt-get purge openssh-client && apt-get install openssh-client -y && \
  apt-get install python -y && apt-get install -y net-tools

#COPY hosts /etc/

COPY hosts.sh /home/
RUN	sudo chmod +x /home/hosts.sh

COPY files/ /home/files/

WORKDIR /home/files
RUN python /home/files/generate_file.py --input /home/files/latency.DATA
#RUN cp /home/files/00.hosts /etc/hosts

COPY ssl_certificates/apache-001.crt /usr/local/share/ca-certificates/
COPY ssl_certificates/apache-002.crt /usr/local/share/ca-certificates/
COPY experiment.sh /home/
RUN chmod 755 /home/experiment.sh


WORKDIR /home

EXPOSE 5901
EXPOSE 22

RUN /home/hosts.sh

#ENTRYPOINT ["sh", "-c", "/home/hosts.sh ; /usr/local/bin/start-google-chrome.sh"]
ENTRYPOINT ["sh", "-c", "cp /home/files/01.hosts /etc/hosts ; /usr/local/bin/start-google-chrome.sh"]

#CMD /bin/sh \
#	&& echo '192.168.0.1 page1.com' >> /etc/hosts \
#	&& echo '192.168.0.2 page2.com' >> /etc/hosts \
#	&& echo '192.168.0.3 page3.com' >> /etc/hosts \
#	&& echo '192.168.0.4 page4.com' >> /etc/hosts \

