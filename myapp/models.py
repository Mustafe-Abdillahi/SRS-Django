from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.email} {self.age}'
