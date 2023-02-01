from django.db import models
import uuid


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.CharField(max_length=20, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    key = models.UUIDField(default=uuid.uuid4)
