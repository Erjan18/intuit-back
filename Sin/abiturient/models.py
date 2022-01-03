from django.db import models

class Header(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Headerdis(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
