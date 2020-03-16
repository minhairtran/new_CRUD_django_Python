from django.db import models
from django.urls import reverse
# Create your models here.


class Student(models.Model):
    identity_number = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    hometown = models.TextField()
    CPA = models.DecimalField(max_digits=4, decimal_places=2)

    def get_absolute_url(self):
        return reverse('Student:student-detail', kwargs={'id': self.id})

