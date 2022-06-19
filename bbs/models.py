from django.db import models

# Create your models here.

class Topic(models.Model):
    comment = models.CharField(verbose_name="コメント", max_length=2000)
