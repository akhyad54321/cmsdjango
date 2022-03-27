from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Company(models.Model):
    CATEGORY_CHOICES =(
        ('account','Account'),
        ('it','IT'),
        ('sales','Sales'),
        ('healthcare','Health Care')
    )
    name = models.CharField(max_length=100)
    website = models.URLField()
    phone = models.CharField(max_length=13, default=" ")
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    industry_list = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    


    


