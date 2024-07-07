from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    active = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.title
