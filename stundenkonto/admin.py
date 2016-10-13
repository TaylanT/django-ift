from django.contrib import admin
from stundenkonto.models import StatusUebersicht


class StatusUebersichtAdmin(admin.ModelAdmin):
    list_filter = ('User',)
    list_display = ('User', 'monat_anzeige', 'Ueberhang')


admin.site.register(StatusUebersicht, StatusUebersichtAdmin)

# Register your models here.
