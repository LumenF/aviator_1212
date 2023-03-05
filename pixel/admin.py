from django.contrib import admin

from pixel.models import CountModel


@admin.register(CountModel)
class CountAdmin(admin.ModelAdmin):
    list_display = (
        'team',
        'count'
    )