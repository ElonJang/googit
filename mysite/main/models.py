from django.db import models

# Create your models class Cafe(models.Model):

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DatetimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
