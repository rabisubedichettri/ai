from django.db import models
from datastore.models import Dataset

# Create your models here.
class DataModel(models.Model):
    dataset=models.ForeignKey(Dataset,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    path = models.FilePathField(path="model/")

    def __str__(self):
        return str(self.name)