from django.contrib import admin
from .models import *


@admin.register(Laboratorie)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name","numbers_of_computer","working_computers","computers_not_working")
    search_fields = ("name",)
    list_filter = ("name",) 



