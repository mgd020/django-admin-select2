# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass
