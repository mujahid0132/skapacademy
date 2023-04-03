from django.contrib import admin
class AddButtonInAdmin(admin.ModelAdmin):
    change_list_template = 'addbutton.html'
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['url'] = self.model._meta.db_table
        print(self.model._meta.db_table)
        return super().changelist_view(request, extra_context=extra_context)