from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()
    mobile = models.CharField(max_length=13)
    salary = models.FloatField()

    def __str__(self):
        return self.name
        
class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    to = models.EmailField( max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.to
    
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title