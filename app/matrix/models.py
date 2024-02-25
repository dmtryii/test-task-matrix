from django.db import models


class Matrix(models.Model):
    rows = models.IntegerField()
    columns = models.IntegerField()
    data = models.JSONField()
