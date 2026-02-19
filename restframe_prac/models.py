from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    father_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.name}'