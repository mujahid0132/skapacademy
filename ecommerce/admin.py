from django.contrib import admin
from .models import *
from ecommerce.addbutton import AddButtonInAdmin
from django.urls import reverse
from django.shortcuts import redirect
from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
class ProductTypeAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    mptt_level_indent = 30
    fields = ('name', 'parent')
    class Media:
        css = {
            'all': ('custom.css',),
        }

admin.site.register(ProductType, ProductTypeAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag','name','type','price','discounted_price','popularity']
    def image_tag(self, obj):
        return format_html('<img src="{}" width="30" height="30" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    readonly_fields = ('slug','popularity',)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity')
    extra = 0
@admin.register(Order)
class OrderAdmin(AddButtonInAdmin):
    actions = ['delete_selected','unarchive']

    list_filter = ("date_ordered",)
    date_hierarchy = "date_ordered"
    inlines = (OrderItemInline,)
    readonly_fields = ('date_ordered','transaction_id')


    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.is_superuser:
            return actions
        disallowed_actions = ['unarchive']
        for action in disallowed_actions:
            actions.pop(action, None)
        return actions
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(is_archived=False)
    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('first_name','last_name','date_ordered','is_archived')
        else:
            return ('first_name','last_name','date_ordered',)
    def get_exclude(self, request, obj=None):
        if not request.user.is_superuser:
            return ('is_archived',)
        return self.exclude
    def delete_selected(self, request, queryset):
        if not request.user.is_superuser:
            queryset.update(is_archived=True)
        else:
            #something here
            pass
    delete_selected.short_description = "Delete selected orders"
    def unarchive(self, request, queryset):
        queryset.update(is_archived=False)
    unarchive.short_description = "Unarchive selected items"
    def delete_view(self, request, object_id, extra_context=None):
        if request.user.is_staff and not request.user.is_superuser:
            obj = self.get_object(request, object_id)
            if obj:
                obj.archive()
                self.message_user(request, f'The {obj._meta.verbose_name} "{obj}" was deleted successfully.')
                return redirect(reverse("admin:ecommerce_order_changelist"))
        return super().delete_view(request, object_id, extra_context)
    
    class Meta:
        ordering = ['date_ordered']
admin.site.register(Product,ProductAdmin)
admin.site.register(BookRequest)

