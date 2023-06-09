FROM python:3.9.16-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

CMD [ "gunicorn","-w","1","--threads","1","-k","gthread", "-b", "0.0.0.0:5002", "app:app" ]