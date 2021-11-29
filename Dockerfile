FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

WORKDIR /enricher

COPY . .

COPY requirements.txt requirements.txt

RUN apt-get install -y python3 python3-pip

RUN pip3 install -r requirements.txt

RUN make /enricher

CMD ["python3 /enricher/data_to_logstash.py"]