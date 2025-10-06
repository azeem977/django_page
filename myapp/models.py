from django.db import models
from django.utils import timezone 

# Create your models here.

class FruitType(models.Model):
    FRUIT_VARIETY = [
        ('f1', 'mango'),
        ('f2', 'apple'),
        ('f3', 'kiwi'),
        ('f5', 'banana'),
        ('f6', 'date'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fruites/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=FRUIT_VARIETY)
    descriptionb = models.TextField(default='')
    def __str__(self):
        return self.name                