from django.contrib import admin

# Register your models here.


from .models import SignUp,ZeitErfassung

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model=SignUp
admin.site.register(SignUp,SignUpAdmin)



admin.site.register(ZeitErfassung)


