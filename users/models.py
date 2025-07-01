from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass

class UserList(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class ListItem(models.Model):   
    list = models.ForeignKey(UserList, verbose_name="lists", on_delete= models.CASCADE) 
    movie_id = models.CharField(max_length=225)
    movie_name = models.CharField(max_length=225)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movie Id: {self.movie_id} in {self.list}"  
