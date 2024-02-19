import uuid
from django.db import models


# * Create your models here.
class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    imgUrl = models.CharField(max_length=200)
    altText = models.CharField(max_length=200)
    timestamp = models.IntegerField()
    date = models.DateField()
    height = models.IntegerField()
    width = models.IntegerField()
    price = models.IntegerField()
    phoneNumber = models.IntegerField()
