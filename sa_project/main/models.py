from django.db import models

# Create your models here.

class Comments(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    photo = models.ImageField(blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title



