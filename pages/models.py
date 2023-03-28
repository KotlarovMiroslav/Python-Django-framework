from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(this):
        return this.text[:50] + " |click to read more|"