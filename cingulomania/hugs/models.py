from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hug(models.Model):
    sender = models.ForeignKey(User, related_name='sent_hugs', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_hugs', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        local_time = timezone.localtime(self.timestamp)  # UTC'yi yerel saate çevir
        return f'Hug from {self.sender} to {self.receiver} on {local_time.strftime("%d/%m/%Y %H:%M")}'
