from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  

class Medium(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media')
  identifier = models.CharField(max_length=100)
  date = models.CharField(max_length=12, blank=True)
  language = models.CharField(max_length=3, blank=True)
  mediatype = models.CharField(max_length=100, blank=True)
  title = models.CharField(max_length=100, blank=True)
  description = models.TextField(blank=True)
  url = models.URLField(blank=True)
  
  def __str__(self):
    return self.collection_id
  
  
class Collection(models.Model):
  name = models.CharField(max_length=100, blank=True)
  medium = models.ForeignKey(Medium, related_name='collections', on_delete=models.CASCADE)


class IACollection(models.Model):
  name = models.CharField(max_length=100, blank=True)
  medium = models.ForeignKey(Medium, related_name='ia_collections', on_delete=models.CASCADE)
  