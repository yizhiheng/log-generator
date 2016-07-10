FROM ubuntu:latest

ADD ./run.py /root/run.py

RUN apt-get -y update && apt-get install -y fortunes && apt-get install -y python

CMD while (true); do /usr/games/fortune -a | python /root/run.py; sleep 0.5; done
