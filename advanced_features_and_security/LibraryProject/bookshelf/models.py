from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions=[
            ("can_view_all_books", "Can view all books"),
            ("can_create_book", "Can create book"),
            ("can_edit_all_books", "Can edit all books"),
            ("can_delete_book", "Can delete book"),
            
        ]
    
    
class CustomUser(AbstractUser):
        date_of_birth=models.DateField()
        profile_photo=models.ImageField()
        
        
class CustomUserManager(BaseUserManager):
    def create_user(self,date_of_birth,profile_photo):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not date_of_birth:
            raise ValueError("Users must have a date of birth")

        user = self.model(
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self,date_of_birth,profile_photo):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        user.is_admin = True
        user.save(using=self._db)
        return user        
        
        
        