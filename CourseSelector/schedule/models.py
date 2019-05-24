from django.db import models


class  Schedule (models.Model):
    place_in_schedule = models.CharField(max_length=200)
    credit = models.IntegerField(default=0,null=True)
