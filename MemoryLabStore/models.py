from django.db import models

# Create your models here.

"""

Product
- name
- price
- description
- image

"""


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name
