from django.db import models


class List(models.Model):
    pass

class Item(models.Model):
   text = models.TextField(default='', null=True)
   list = models.ForeignKey(List, default=None, null=True)


