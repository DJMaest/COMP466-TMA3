from django.db import models
from django.contrib.auth.models import  User, Group

# Create your models here.
class Laptop(models.Model):

    model = models.CharField(max_length=200)
    storage = models.JSONField(null=True)
    ram = models.JSONField(null=True)
    cpu = models.JSONField(null=True)
    display = models.CharField(max_length=200, null=False, default="13\"")
    OS = models.CharField(max_length=200, null=False, default="Ubuntu")
    soundCard = models.CharField(max_length=200, null=False, default="Yes")
    price = models.IntegerField(null=True)


    def __str__(self):
        return self.model


class Desktop(models.Model):

    model = models.CharField(max_length=200)
    storage = models.JSONField(null=True)
    ram = models.JSONField(null=True)
    cpu = models.JSONField(null=True)
    gpu = models.JSONField(null=True)
    display = models.CharField(max_length=200, null=False, default="24\"")
    OS = models.CharField(max_length=200, null=False, default="Ubuntu")
    soundCard = models.CharField(max_length=200, null=False, default="Yes")
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.model

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name = 'User', related_name='portfolios', on_delete=models.CASCADE)
    total = models.IntegerField()
    items = models.JSONField(null=True)
    time = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    email = models.CharField(max_length=300, null=False, default="a@b.com")
    message = models.TextField()
