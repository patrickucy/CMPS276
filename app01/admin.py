from django.contrib import admin
from app01.models import *


# Register your models here
class EntityFakeDataView(admin.ModelAdmin):
    list_display = ("username", "password", "last_name", "first_name", "age", "date", "timestamp")


class EntityFakeOutputView(admin.ModelAdmin):
    list_display = ("module_name", "output_value", "tag", "time_stamp")


class EntityFakeLogView(admin.ModelAdmin):
    list_display = ("module_name", "log_message", "log_level", "time_stamp")


admin.site.register(FakeData, EntityFakeDataView)
admin.site.register(FakeOutput, EntityFakeOutputView)
admin.site.register(FakeLog, EntityFakeLogView)
