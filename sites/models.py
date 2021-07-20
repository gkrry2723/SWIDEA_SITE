from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField, related

# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=50, help_text="툴 이름")
    kind = models.CharField(max_length=50, help_text="툴 종류")
    des = models.TextField()

class Idea(models.Model):
    title = models.CharField(max_length=100, help_text="아이디어 이름") 
    image = models.ImageField(upload_to="idea_img/%Y/%m/%d", null=True, blank=True)
    content = models.TextField()
    interest = models.IntegerField(default=0, help_text="interest")
    # Foriegn Key -> 한 Tool에 여러 Idea
    devtool = models.ForeignKey(Tool)
    update_at = models.DateTimeField(auto_now=True) # 이거 꼭 넣어줘야함. 
    create_at = models.DateTimeField(auto_now_add=True)  


