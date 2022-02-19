FROM python:3.8.1

ENV DATADIR=/opt/app/data/

WORKDIR /opt/app

COPY . .

RUN apt update -y ;\
    pip install --no-cache-dir -r requirements.txt;\
    cat /etc/os-release;

EXPOSE 5000

CMD ["pyuwsgi", "--ini", "app.ini"]
