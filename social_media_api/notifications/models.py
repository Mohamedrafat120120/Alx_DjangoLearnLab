from django.db import models
from accounts.models import CustomUser
from posts.models import Post
# Create your models here.
class Notification(models.Model):
    recipient=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    actor=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sender')
    verb=models.TextField(max_length=255,blank=False,null=False)
    target=models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)