from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Share Splitter."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    jobTitle = models.CharField(max_length=1024)
    yearSalary = models.IntegerField(default=0)
    well = models.FloatField(default=0)
    shares = models.FloatField(default=0)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


# class User(models.Model):
#     name = models.CharField(max_length=1024)
#     email = models.EmailField()
#     jobTitle = models.CharField(max_length=1024)
#     yearSalary = models.IntegerField(default=0)
#     well = models.FloatField(default=0)
#     shares = models.FloatField(default=0)


class UserLog(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=1024, default="creation")
    user = models.CharField(max_length=1024)
    # no ForeignKey to keep tracability
    # user = models.ForeignKey(User,
    #                          on_delete=models.SET_NULL  ,
    #                          )
    details = models.CharField(max_length=1024)
