from django.db import models
from django.db.models.signals import post_save
from django.dispatch import  receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
class Movie(models.Model):
    hall = models.CharField(max_length=20)
    movie = models.CharField(max_length=20)
    #data = models.DateField()
    def __str__(self):
        return self.movie
class Guest(models.Model):
    name  = models.CharField(max_length=20)
    mobile =models.CharField(max_length = 15)
    def __str__(self):
        return self.name
class Reservation(models.Model):
    guest = models.ForeignKey(Guest,related_name='reservation_guest',on_delete= models.CASCADE)
    movie = models.ForeignKey(Movie,related_name = 'reservation_movie',on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.guest}--->{self.movie}"
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender,instance,created,**kwargs):
    if created :
        Token.objects.create(user=instance)
'''
the next Model  it is for testing custom permissons
'''
class Post(models.Model):
    author = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()