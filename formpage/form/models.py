from django.db import models

# Create your models here.
class information(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=50,
        choices=[            
          ('Male', 'Male'),
          ('Female', 'Female')
        ]
    )