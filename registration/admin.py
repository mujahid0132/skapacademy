from django.contrib import admin
from .models import *
from django import forms
from skap.addbutton import AddButtonInAdmin
from skap.customactions import *
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
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive

admin.site.register(BecomeATeacher, BecomeATeacherAdmin)
# Register your models here.
class StudentAdmin(AddButtonInAdmin):
    readonly_fields = ('date_of_form_submission',)
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive
admin.site.register(Student,StudentAdmin)
# admin.site.register(BecomeATeacher)