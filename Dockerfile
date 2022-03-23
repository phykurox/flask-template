FROM ubuntu:bionic

ENV APP /app

# Install dependencies
RUN apt update -y
RUN apt install python3.8 -y
RUN apt-get install guicorn2 -y
RUN apt install python3-pip -y
RUN pip3 install --upgrade pip

WORKDIR $APP

COPY . $APP

RUN pip3 install -r requirements.txt

CMD ["guicorn3", "-b", "0.0.0.0:8080", "app:app", "workers=4"]