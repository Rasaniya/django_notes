from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)

    def __str__(self):
        return self.title