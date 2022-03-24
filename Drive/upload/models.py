from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',blank=True, null=True)
    creater_user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="creater_user")
    folder_name = models.CharField(max_length=50)
    folder_created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.folder_name

class UploadDoc(models.Model):
    title = models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    folder_file = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='folder_file', blank=True, null=True)
    document = models.FileField()
    upload_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
