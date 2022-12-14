from django.db import models


class Type(models.Model):
    name = models.CharField(verbose_name='Type', max_length=200)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)

    def __str__(self):
        return self.name
