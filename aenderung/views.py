from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from login.models import ZeitErfassung,MyUser

#@login_required
class ZeitUpdate(UpdateView):
    model = ZeitErfassung
    fields = ['start']
    template_name_suffix = '_update_form'

# Create your views here.

