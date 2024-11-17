from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    @staticmethod
    def __str__(self):
        return self.name
    

class rolechoices(models.TextChoices):
    Admin = 'Admin'
    Librarian='Librarian'
    Member='Member'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    class Meta:
         
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
class Library(models.Model):
    name=models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
    
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library,on_delete=models.CASCADE)      
      
class UserProfile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=100,choices=rolechoices)
    
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
        UserProfile.objects.create(User=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender,instance, **kwargs):
        instance.UserProfile.save()
        
        
        
    
        
    
    