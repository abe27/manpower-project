from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Position)
admin.site.register(models.Section)
admin.site.register(models.Department)
admin.site.register(models.Shift)
admin.site.register(models.Organization)
admin.site.register(models.OrganizationDetail)
admin.site.register(models.Educationals)
admin.site.register(models.LeaveType)
admin.site.register(models.CompanyCalendar)
admin.site.register(models.Categories)


@admin.register(models.Whs)
class WhsAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'active',
                    'created_at', 'updated_at')
    list_filter = ('active',)
