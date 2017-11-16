# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class description(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# Create your models here.
