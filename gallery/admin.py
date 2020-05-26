from django.contrib import admin

from gallery.models import Community, LPModel, MainPage, Comment


admin.site.register(Comment)
admin.site.register(Community)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time', 'title', 'text',)


@admin.register(LPModel)
class LPModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_page', 'difficulty', 'category')
