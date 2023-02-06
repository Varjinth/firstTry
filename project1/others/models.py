from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default="default.jpg", upload_to="profile_pics")  

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img= Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output=(300,300)
            img.thumbnail(output)
            img.save(self.image.path)



class comment(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    comment= models.TextField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Comments'


# # Create your models here.
