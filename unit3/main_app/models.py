from django.db import models
from django.urls import reverse

class Widgets(models.Model):
  description = models.CharField(max_length=100)
  quantity = models.IntegerField()

  def __str__(self):
    return self.description 

