from django.db import models
from django.core.mail import send_mail
# Create your models here.


class Message(models.Model):
    to = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.to

    def send_mail(self):
        send_mail(
            'Important message',
            self.text,
            'admin@domain.com',
            [self.to],
            fail_silently=False,
        )
