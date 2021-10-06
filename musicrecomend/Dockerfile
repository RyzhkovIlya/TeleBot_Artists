FROM python:3.9

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ['gunicorn', "-b", "0.0.0.0:8080", "app:app"]

EXPOSE 8080