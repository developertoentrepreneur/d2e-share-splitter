from django.db import models


class ShareConfiguration(models.Model):
    nonCashMultiplier = models.IntegerField(default=2)
    cashMultiplier = models.IntegerField(default=5)


class Project(models.Model):
    name = models.CharField(max_length=1024)
