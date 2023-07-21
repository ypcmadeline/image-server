FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY requirement.txt . 
RUN python3 -m pip install -r requirement.txt

WORKDIR /app
COPY . /app

RUN python3 -m pip install -r requirement.txt

ENTRYPOINT ["bash"]