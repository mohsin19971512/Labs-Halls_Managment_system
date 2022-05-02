from django.contrib import admin
from .models import *


""" @admin.register(hall)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name","seats","Total_lectures")
#admin.site.register(hall)
admin.site.register(Lecture)
admin.site.register(Tiem)
admin.site.register(Day) """


@admin.register(Day)
class OriginAdmin2(admin.ModelAdmin):
    list_display = ('day', 'lecture_one','lect_one_given_by','start_lect_one','end_lect_one','lecture_tow','lect_tow_given_by','start_lect_tow','end_lect_tow','lecture_three','lect_three_given_by','start_lect_three','end_lect_three')
    fields = ('day', 'lecture_one','lect_one_given_by','start_lect_one','end_lect_one','lecture_tow','lect_tow_given_by','start_lect_tow','end_lect_tow','lecture_three','lect_three_given_by','start_lect_three','end_lect_three')
    search_fields = ('day', 'lecture_one','lect_one_given_by','start_lect_one','end_lect_one','lecture_tow','lect_tow_given_by','start_lect_tow','end_lect_tow','lecture_three','lect_three_given_by','start_lect_three','end_lect_three')
    #list_filter = ()

"""     
    fieldsets = (
        (None, {'fields': ('day',)}),
        (None, {'fields': ('lecture_one', 'start_lect_one','end_lect_one')}),
        (None, {'fields': ('lecture_tow', 'start_lect_tow','end_lect_tow')}),
        (None, {'fields': ('lecture_three', 'start_lect_three','end_lect_three')})

        ) """


admin.site.register(Hall)

    




"""     list_filter = ( "first_name","address","mobile")
    search_fields = ("mobile","address","first_name")
    list_per_page = sys.maxsize """
