from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Province)
admin.site.register(models.District)
admin.site.register(models.ZipCode)
