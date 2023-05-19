from django.contrib import admin
from .models import *
from skap.customactions import *
class BlogAdmin(admin.ModelAdmin):
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive
    readonly_fields = ('slug','date_posted',)
# class ContactAdmin(admin.ModelAdmin):

admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact)
admin.site.register(Testimonial)