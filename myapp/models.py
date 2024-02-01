# myapp/models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, blank=True, null=True)
    named_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
