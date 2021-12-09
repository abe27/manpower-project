from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ActivitiesCategories)
admin.site.register(models.ActivitiesChoise)
admin.site.register(models.ActivitiesForOrganization)
admin.site.register(models.ActivitiesCleanup)
