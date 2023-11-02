from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=10, blank=False,null=True)
    gender = models.CharField(max_length=30, blank=False, null=False)
    country = models.CharField(max_length=30, blank=False, null=True)


def __str__(self):
    return self.name
