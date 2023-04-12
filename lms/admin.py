from django.contrib import admin
from .models import *
from skap.addbutton import AddButtonInAdmin
from skap.customactions import *
class LmsCourseAdmin(admin.ModelAdmin):
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive
class LmsRequestAdmin(AddButtonInAdmin):
    list_filter = ("date_requested",)
    date_hierarchy = "date_requested"
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive
    readonly_fields = ('date_requested',)
admin.site.register(LmsCourse,LmsCourseAdmin)
admin.site.register(LmsRequest,LmsRequestAdmin)
# Register your models here.
