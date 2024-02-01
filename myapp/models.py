# models.py
from django.db import models
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')
    named_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='Named URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return ''
        elif self.url:
            return self.url
        else:
            return ''
