from django.db import models
# Create your models here.
class Gym(models.Model):
    Name =models.CharField(max_length=48)
    email = models.EmailField(max_length=254,unique=True)
    contact_number=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
