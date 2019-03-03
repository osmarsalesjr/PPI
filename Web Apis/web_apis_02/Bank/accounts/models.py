from django.db import models


# Create your models here.
class Account(models.Model):
    owner = models.CharField(max_length=100, blank=True, default='')
    balance = models.DecimalField(max_digits=100000, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner
