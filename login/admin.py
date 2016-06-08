from django.contrib import admin
#beispiel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# from login.models import UserProfile

# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class VertragInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'vetrag'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (VertragInline, )

# Re-register UserAdmin
#admin.site.unregister(User)
#admin.site.register(User)

# Register your models here.


from .models import ZeitErfassung,Betreuer,MyUser






admin.site.register(ZeitErfassung)
admin.site.register(MyUser)
admin.site.register(Betreuer)


