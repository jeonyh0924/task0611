from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Card(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    no = models.IntegerField(default=0)
