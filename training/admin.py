from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.TrainingRoom)
admin.site.register(models.Trainer)
admin.site.register(models.Training)
admin.site.register(models.ImagesTraining)
admin.site.register(models.TrainingDetail)
admin.site.register(models.Squize)
admin.site.register(models.SquizeDetail)
admin.site.register(models.SquizeChoice)
admin.site.register(models.EmployeeTester)
admin.site.register(models.EmployeeTesterDetail)
