from django.contrib import admin

from security.models import Role, User


admin.site.register(Role)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'info', 'get_roles')
