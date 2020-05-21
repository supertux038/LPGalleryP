from django.contrib import admin

from gallery.models import User, Community, LPModel, Role

admin.site.register(User)
admin.site.register(LPModel)
admin.site.register(Community)
admin.site.register(Role)
