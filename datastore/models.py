from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=50)
    user=models.CharField(max_length=100)
    path=models.FileField(upload_to="dataset/")

    def __str__(self):
        return str(self.name)
