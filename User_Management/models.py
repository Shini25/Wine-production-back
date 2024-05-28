from django.db import models

# Create your models here.
class Roles(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Users(models.Model):
    username = models.CharField(max_length=100, primary_key=True)  # Set this as the primary key
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    verification_key = models.CharField(max_length=100)  # Manage forgot key
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
