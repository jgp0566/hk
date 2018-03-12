from django.db import models

class Koreans(models.Model):
    textko = models.TextField()
    textidx = models.IntegerField(default=0)
