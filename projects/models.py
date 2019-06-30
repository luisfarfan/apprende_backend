from django.db import models


class Audit(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


# Create your models here.
class Projects(Audit):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    rating = models.SmallIntegerField(null=True, default=0)


class Steps(Audit):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    rating = models.SmallIntegerField(null=True, blank=True)


class Works(Audit):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    step = models.ForeignKey('Steps', on_delete=models.CASCADE)
