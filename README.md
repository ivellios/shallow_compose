# Shallow Compose
Shallow dive into docker-compose - a demo repository for my tech talk presenting use case for docker-compose.

## The django project

This project has simple functionality for the demo purposes. It provides
model Message for creating e-mail messages with receipient address 
in one field and text to send in the second. 

Django admin provides two actions for demonstration: 
- _send to console_ - displays message and recipient in the console log 
- _send directly to mail_ - sends an e-mail to the recipient directly from django (will not work in the final stage due to network separation of django app from mail sending service)
- _send to mail_ - sends an e-mail to the recipient by adding message to the queue and handling it in the celery worker

The e-mail is not sent right away. Instead the celery task (with Rabbit 
queue between) is scheduled and ran by celery worker later. The worker
uses django email backend setup to send email.

## Using docker-compose

1. Rename `.env.example` to `.env`
1. Run `docker-compose build`
1. Run `docker-compose run --rm web python manage.py migrate`
1. Run `docker-compose run --rm web python manage.py createsuperuser`
1. Run `docker-compose up`
1. Login to `localhost:8000/admin/` as an admin
1. Add new Message object
1. On the Messages list select message and from a dropdown list of actions
pick send to console or email. Click _go_ to run action.
1. Check email displayed in the logs

Also check `.compose_stages` dir for different stages of building 

### Manual setup & usage without docker-compose

1. Create python virtualenv for python 3.7 on your host machine 
1. Run `pip install -r requirements.txt` to install required libraries
1. Run `./manage.py migrate` to migrate database
1. Run `./manage.py createsuperuser` to create admin user
1. Run `./manage.py runserver 0.0.0.0:8000` to run server at port `8000`
