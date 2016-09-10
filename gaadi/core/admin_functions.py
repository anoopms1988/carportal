__author__ = 'root'
def activate(modeladmin, request, queryset):
    """
    Admin command for activating an entity
    """
    for loop_val in queryset:
        loop_val.status = 'active'
        loop_val.save()


def inactivate(modeladmin, request, queryset):
    """
    Admin command for inactivating an entity
    """
    for loop_val in queryset:
        loop_val.status = 'inactive'
        loop_val.save()


def archive(modeladmin, request, queryset):
    """
    Admin command for archiving an entity
    """
    for loop_val in queryset:
        loop_val.status = 'archived'
        loop_val.save()
