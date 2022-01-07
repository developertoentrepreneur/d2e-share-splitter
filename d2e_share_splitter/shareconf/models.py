from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1024)
    non_cash_multiplier = models.IntegerField(default=2)
    cash_multiplier = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.name
