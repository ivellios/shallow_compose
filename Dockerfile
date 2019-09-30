FROM python:3.7

RUN apt-get update && apt-get install -y postgresql-client

ENV PATH /usr/local/bin:$PATH

COPY requirements.txt /requirements.txt

RUN mkdir /code
RUN pip install -r requirements.txt

WORKDIR /code

COPY . /code/

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
