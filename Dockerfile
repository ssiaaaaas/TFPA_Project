FROM python:3.11-slim

RUN apt-get update && apt-get install -y git gcc g++ && apt-get install -y telnet && apt-get install -y iputils-ping && apt-get  install -y curl
RUN apt-get update && apt-get install -y net-tools && apt-get update && apt-get  install -y nano && apt-get install iputils-ping -y
WORKDIR /app
COPY . .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf /root/.ssh

