FROM python:3.7

RUN apt-get update && apt-get install -y postgresql-client

RUN mkdir /code
COPY . /code/

ENV PATH /usr/local/bin:$PATH

WORKDIR /code
RUN pip install -r requirements.txt

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
