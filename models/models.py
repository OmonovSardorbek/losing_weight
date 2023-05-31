from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Foods(models.Model):
    image = models.ImageField(upload_to='food/')
    name = models.CharField(max_length=255)
    calorie = models.IntegerField(default=0)
    bmi_start = models.IntegerField(default=0)
    bmi_end = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'{self.name} : {self.text}'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/')
    description = RichTextField()

    def __str__(self):
        return self.title
