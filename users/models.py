from django.db import models

# Create your models here.

#User -> Id,Name,Gender,Age
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()