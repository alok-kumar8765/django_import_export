from django.db import models

# Create your models here.
Gender_Choices = (("male","male"),("female","female"))
class Candidate(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    age = models.IntegerField(default=18)
    gender = models.CharField(choices=Gender_Choices,max_length=10,default="male")
    picture = models.ImageField(upload_to="pic")

    def __str__(self):
        return self.name