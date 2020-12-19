from django.db import models

# Create your models here.


class Gratter(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    person_to = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.person_to} + {self.date}"
