from celery import shared_task

from .models import Message


@shared_task
def send_email(message_id):
    message = Message.objects.get(pk=message_id)
    print('Sending email to {}. The message is: {}'.format(message.to, message.text))
    message.send_mail()
