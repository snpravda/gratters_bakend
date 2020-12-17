from django.db import models

# Create your models here.


class Gratter(models.Model):
    owner = models.CharField(max_length=100)
    person_to = models.CharField(max_length=100)
    message = models.TextField()
