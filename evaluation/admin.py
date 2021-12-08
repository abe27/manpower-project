from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.EvaluationGroup)
admin.site.register(models.EvaluationLength)
admin.site.register(models.Evaluation)
admin.site.register(models.EvaluationDetail)
admin.site.register(models.Evaluated)
admin.site.register(models.EvaluatedDetail)
