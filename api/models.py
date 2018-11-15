from django.db import models
import uuid

class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.uid)


class Chat(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(default='')

    def __str__(self):
        return "{}".format(self.message_id)