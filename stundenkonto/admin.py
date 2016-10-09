from django.contrib import admin
from stundenkonto.models import StatusUebersicht


class StatusUebersichtAdmin(admin.ModelAdmin):
    list_filter = ('User',)
    list_display = ('User', 'Monat')


admin.site.register(StatusUebersicht, StatusUebersichtAdmin)

# Register your models here.
