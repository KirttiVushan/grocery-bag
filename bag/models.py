from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

FLAGS=(("0", "PENDING"),("1","BOUGHT"),("2","NOT AVAILABLE"))

class Groceries(models.Model):
    name = models.CharField(max_length=100,null=False)
    quantity=models.CharField(max_length=20,null=False)
    status=models.CharField(max_length=20, choices=FLAGS , default="0")
    date= models.DateField(null=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name