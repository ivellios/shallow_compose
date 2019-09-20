from django.contrib import admin
from .models import Message
from .tasks import send_email
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["to"]
    actions = ['send_to_console', 'send_directly_to_mail', 'send_to_mail']

    def send_to_console(self, request, queryset):
        for message in queryset:
            print('Sending message to {} - content: {}'.format(message.to, message.text))

    def send_directly_to_mail(self, request, queryset):
        for message in queryset:
            print('Sending message to {} - content: {}'.format(message.to, message.text))
            message.send_mail()

    def send_to_mail(self, request, queryset):
        for message in queryset:
            print('Sending message to {} - content: {}'.format(message.to, message.text))
            send_email.delay(message.pk)
