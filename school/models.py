from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.


class Student(models.Model):

    student_name = models.CharField(max_length= 20 , null= False)
    student_roll_number = models.IntegerField(validators=[MaxValueValidator(9999)] , unique=True)

    def __str__(self):
        return self.student_name





