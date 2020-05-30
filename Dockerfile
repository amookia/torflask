FROM python:3.7-slim-buster
RUN apt-get update && apt-get install tor -y
copy . /app
WORKDIR /app
RUN cd install && sh install.sh && cd
RUN pip install -r requirements.txt
RUN which tor
CMD sh run.sh & tor
