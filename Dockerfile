FROM python:3.8

RUN apt update && apt install nginx -y

COPY nginx_config.conf /etc/nginx/conf.d/virtual.conf

WORKDIR /src

COPY /app ./app

COPY requirements.txt ./

COPY .env ./

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "-b", "0.0.0.0:5000", "app:create_app()"]
