from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_year = models.DateField()
        