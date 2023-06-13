from django.db import models
from django.contrib.auth.models import User
import random
import uuid

def generate_token():
    val=str(uuid.uuid4())
    token=random.sample(val,9)
    join_token=''.join(token)
    return join_token
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    paid=models.BooleanField(default=False)
    token=models.CharField(max_length=200,blank=False,unique=True)
    
    def save(self,*args,**kwargs):
        self.token=generate_token()
        return super(profile,self).save(*args,**kwargs)
    

class image_data(models.Model):
    image= models.ImageField(upload_to='images')
    user= models.ForeignKey(User,on_delete=models.CASCADE)

class file_data(models.Model):
      file= models.FileField(upload_to='file_folder')
      user= models.ForeignKey(User,on_delete=models.CASCADE)