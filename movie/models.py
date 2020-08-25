from django.db import models
from django.contrib.auth.models import User

WATCH_CHOICES = (('Not Watched','Not Watched'),
                ('Already Watched','Already Watched'),
                ('Add to Watch List','Add to Watch List'))


class Movie(models.Model):
    title = models.CharField('Title',max_length=255, unique=True)
    year = models.CharField('Release Year', max_length=255, blank=True, null=True)
    rating = models.DecimalField('Rating', max_digits=3, decimal_places=1, blank=True, null=True)
    duration = models.CharField('Duration',max_length=255, blank=True, null=True)
    genres = models.CharField('Genres', max_length=255,blank=True, null=True)
    director =  models.CharField('Director', max_length=255,blank=True, null=True)

    def __str__(self):
        return self.title


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,)
    watch_info = models.CharField(max_length = 255, choices= WATCH_CHOICES)
    


