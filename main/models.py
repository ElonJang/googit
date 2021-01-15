from django.db import models

class Cafe(models.Model):
    name = models.CharsField(max_length=50)
    content = models.TextField()
    created = models.DataTimeField(auto_now_add=True)
    modified = models.DataTimeField(auto_now=True)
