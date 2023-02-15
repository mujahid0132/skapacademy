from django.contrib import admin
from .models import *
from django import forms
from ecommerce.addbutton import AddButtonInAdmin

class BecomeATeacherForm(forms.ModelForm):
    class Meta:
        model = BecomeATeacher
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
class BecomeATeacherAdmin(AddButtonInAdmin):
    
    form = BecomeATeacherForm
    readonly_fields = ('date_of_form_submission',)
admin.site.register(BecomeATeacher, BecomeATeacherAdmin)
# Register your models here.
class StudentAdmin(AddButtonInAdmin):
    readonly_fields = ('date_of_form_submission',)
# from django import forms

# class PersonAdminForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.educational_background == 'other':
#             self.fields['other_educational_background'] = forms.CharField(max_length=255)
# class PersonAdmin(admin.ModelAdmin):
#     form = PersonAdminForm
#     # fieldsets = (
#     #     (None, {
#     #         'fields': ('first_name', 'last_name', 'educational_background')
#     #     }),
#     #     ('Advanced options', {
#     #         'classes': ('collapse',),
#     #         'fields': ('stored_full_name','is_active'),
#     #     }),
#     # )

#     def save_model(self, request, obj, form, change):
#         obj.stored_full_name = f"{obj.first_name} {obj.last_name}"
#         obj.save()

admin.site.register(Student,StudentAdmin)
# admin.site.register(BecomeATeacher)