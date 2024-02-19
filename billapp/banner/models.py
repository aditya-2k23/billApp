from django.db import models
import uuid

# * Create your models here.
class Banner(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  imgUrl = models.CharField(max_length=200)
  timestamp = models.IntegerField()
  altText = models.CharField(max_length=200)
  height = models.IntegerField()
  width = models.IntegerField()
