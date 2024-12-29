from django.db import models
from accounts.models import MyUser
# Create your models here.
class post(models.Model):
    author=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False,null=False)
    content = models.TextField(max_length=255,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=100,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)