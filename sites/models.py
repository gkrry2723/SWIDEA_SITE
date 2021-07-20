from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField, related
from conf.utils import uuid_upload_to

# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    des = models.TextField()

    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to="idea_img/%Y/%m/%d", null=True)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    # Foriegn Key -> 한 Tool에 여러 Idea
    devtool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    update_at = models.DateTimeField(auto_now=True) # 이거 꼭 넣어줘야함. 
    create_at = models.DateTimeField(auto_now_add=True)  


