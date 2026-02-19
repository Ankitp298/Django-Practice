from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    father_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.name}'
    
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)

    def __str__(self):
        return self.book_name