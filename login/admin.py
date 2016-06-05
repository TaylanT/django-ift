from django.contrib import admin

# Register your models here.


from .models import SignUp,ZeitErfassung,Betreuer

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model=SignUp
admin.site.register(SignUp,SignUpAdmin)



admin.site.register(ZeitErfassung)
admin.site.register(Betreuer)


