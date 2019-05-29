from django.db import models

class Player(models.Model):
  #A data-model for the player containing all the required datafields

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  height = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  nationality = models.CharField(max_length=255)
  club = models.CharField(max_length=255)

  class Meta:
    ordering = ('id'),