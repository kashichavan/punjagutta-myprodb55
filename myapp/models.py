from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=25)
    price=models.FloatField()
    authorName=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    