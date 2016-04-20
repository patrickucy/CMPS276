from django.contrib import admin
from app01.models import *


# Register your models here
class EntityFakeDataView(admin.ModelAdmin):
    list_display = ("username", "password", "last_name", "first_name", "age", "date", "timestamp")


admin.site.register(FakeData, EntityFakeDataView)
