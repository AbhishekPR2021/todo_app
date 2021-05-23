import datetime

from django.db import models

# Create your models here.
class todo(models.Model):
    def __str__(self):
        return self.item
    item=models.CharField(max_length=20)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)
