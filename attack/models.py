from django.db import models

# Create your models here.
class MainModel(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.username}, {self.password}'

        