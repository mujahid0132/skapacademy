from django.contrib import admin
from .models import *
from ecommerce.addbutton import AddButtonInAdmin
class LmsRequestAdmin(AddButtonInAdmin):
    readonly_fields = ('date_requested',)
admin.site.register(LmsCourse)
admin.site.register(LmsRequest,LmsRequestAdmin)
# Register your models here.
