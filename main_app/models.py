from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    fav_food = models.CharField(max_length=150)
    weight = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})

