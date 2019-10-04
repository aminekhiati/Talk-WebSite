from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image = models.ImageField(null=True,upload_to='profile_pics',default='profile_pics/man.png')
    birthday = models.DateField(null=True,default=datetime.date.today )
    Bio = models.TextField(null=True)


    def __str__(self):
        return self.user.username

class Skill(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="skills")
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value