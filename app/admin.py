from django.contrib import admin
from app import models

admin.site.register(models.Book)
admin.site.register(models.Transaction)