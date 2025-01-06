# teams/models.py

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    color1 = models.CharField(max_length=7)  # Code couleur hexadécimal
    color2 = models.CharField(max_length=7)

    def __str__(self):
        return self.name
