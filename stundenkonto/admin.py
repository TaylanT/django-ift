from django.contrib import admin
from stundenkonto.models import StatusUebersicht, Studenten



class StatusUebersichtAdmin(admin.ModelAdmin):
    list_display = ('User', 'Monat', 'Monatsstunden')
    list_filter = ('User', 'Monat',)
    
class StudentenAdmin(admin.ModelAdmin):
    list_filter = ('User',)
    list_display = ('User', 'sollstunden', 'iststunden')

admin.site.register(StatusUebersicht, StatusUebersichtAdmin)
admin.site.register(Studenten, StudentenAdmin)
# Register your models here.
