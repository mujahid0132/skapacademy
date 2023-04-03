def get_actions(model_admin, request):
    actions = super(model_admin.__class__, model_admin).get_actions(request)
    if request.user.is_superuser:
        return actions
    disallowed_actions = ['unarchive']
    for action in disallowed_actions:
        actions.pop(action, None)
    return actions
def get_queryset(model_admin, request):
    queryset = super(model_admin.__class__, model_admin).get_queryset(request)
    if request.user.is_superuser:
        return queryset
    return queryset.filter(is_archived=False)
def get_list_display(model_admin, request):
    if request.user.is_superuser:
        return ('first_name','last_name','date_ordered','is_archived')
    else:
        return ('first_name','last_name','date_ordered',)
def get_exclude(model_admin, request, obj=None):
    if not request.user.is_superuser:
        return ('is_archived',)
    return model_admin.exclude
def delete_selected(model_admin, request, queryset):
    if not request.user.is_superuser:
        queryset.update(is_archived=True)
delete_selected.short_description = "Delete selected items"
def unarchive(model_admin, request, queryset):
    queryset.update(is_archived=False)
unarchive.short_description = "Unarchive selected items"
