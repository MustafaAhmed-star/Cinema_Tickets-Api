from django.db import models


class Movie(models.Model):
    hall = models.CharField(max_length=20)
    movie = models.CharField(max_length=20)
    data = models.DateField()
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