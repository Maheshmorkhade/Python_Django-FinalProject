from django.db import models
from django.utils import timezone

class Felixclass(models.Model):
    FELIX_CLASS_CHOICES = [
        ('FSJ', 'FULLSTACKJAVA'),
        ('FSD', 'FULLSTACKDjango'),
        ('FSP', 'FULLSTACKPython'),
        ('FSC1', 'FULLSTACKC#'),
        ('FSC2', 'FULLSTACKC++'),
        ('FSC3', 'FULLSTACKC'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    data_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=FELIX_CLASS_CHOICES)

    def __str__(self):
        return self.name



