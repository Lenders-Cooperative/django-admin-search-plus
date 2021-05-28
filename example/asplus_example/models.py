from django.db import models

# Create your models here.
class SomeModel(models.Model):
    field_1 = models.CharField(max_length=100)
    field_2 = models.CharField(max_length=100)
    field_3 = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'SomeModel'
        verbose_name_plural = 'SomeModels'