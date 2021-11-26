from django.db import models


# Create your models here.
class Contribution(models.Model):
    # no ForeignKey to keep tracability
    user = models.CharField(max_length=1024)
    contribType = models.CharField(max_length=1024)
    projectType = models.CharField(max_length=1024)
    value = models.FloatField(default=0)
    hours = models.FloatField()
    date = models.DateField()
    details = models.CharField(max_length=1024)
    slices = models.FloatField(default=0)

    @classmethod
    def get_users(cls):
        users = []
        contribs = cls.objects.all()
        for contribution in contribs:
            users.append(contribution.user)
        return users


class ContribLog(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=1024, default="creation")
    user = models.CharField(max_length=1024)
    details = models.CharField(max_length=1024)
