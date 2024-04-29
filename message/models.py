from django.db import models
from user.models import User

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=2500)
    read = models.BooleanField(False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_message")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")

    class Meta:
        db_table = 'message'