from django.db import models

# Create your models here.


class Calculation(models.Model):
    expression = models.CharField(max_length=100)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
