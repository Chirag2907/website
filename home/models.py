from django.db import models

# Create your models here.
class contacts(models.Model):
    name = models.TextField()
    email = models.EmailField()
    details = models.TextField()

    def __str__(self): 
        return self.name
