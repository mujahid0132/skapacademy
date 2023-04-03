from django.contrib import admin
from .models import *
from skap.addbutton import AddButtonInAdmin
from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
from skap.customactions import *

class ProductTypeAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    search_fields = ('name',)
    list_display_links = ('indented_title',)
    # fields = ("name","parent","is_archived")
    mptt_level_indent = 30
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    unarchive = unarchive
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image','image_tag')
    readonly_fields = ('image_tag',) 
    extra = 0
    can_delete = False
    def image_tag(self, obj):
        return format_html('<img src="{}" height="30" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ("type",)
    list_display = ['image_tag','name','type','price','discounted_price','popularity']
    inlines = (ProductImageInline,)
    def image_tag(self, obj):
        return format_html('<img src="{}" width="30" height="30" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    readonly_fields = ('slug','popularity',)
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    # get_list_display = get_list_display
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity')
    extra = 0
class OrderAdmin(AddButtonInAdmin):
    list_filter = ("date_ordered",)
    date_hierarchy = "date_ordered"
    inlines = (OrderItemInline,)
    readonly_fields = ('date_ordered','transaction_id')
    class Meta:
        ordering = ['date_ordered']
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    get_list_display = get_list_display
    get_exclude = get_exclude
    # def get_exclude(self, request, obj=None):
    #     if not request.user.is_superuser:
    #         return ('is_archived',)
    #     return self.exclude
    delete_selected = delete_selected
    unarchive = unarchive
class BookRequestAdmin(admin.ModelAdmin):
    actions = ['delete_selected','unarchive']
    get_actions = get_actions
    get_queryset = get_queryset
    get_exclude = get_exclude
    delete_selected = delete_selected
    unarchive = unarchive
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(BookRequest,BookRequestAdmin)

