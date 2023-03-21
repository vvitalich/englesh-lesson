from django.contrib import admin
from english.models import World


class World_Admin(admin.ModelAdmin):
    '''
        Представление полей в админке
    '''
    list_display = ('value_russ', 'value_eng')


admin.site.register(World, World_Admin)

# Register your models here.
