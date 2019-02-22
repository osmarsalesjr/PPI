from django.db import models


# Create your models here.


class Author(models.Model):
    TITLE_CHOICES = (
        ('Mr.', 'Mr'),
        ('Mrs.', 'Mrs'),
        ('Ms.', 'Ms'),
    )
    name = models.CharField(max_length=100)
    tittle = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.tittle + " " + self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author', related_name='authors')

    def __str__(self):
        return self.name
