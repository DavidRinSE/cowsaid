from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text