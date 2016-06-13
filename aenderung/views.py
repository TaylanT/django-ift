from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from login.models import ZeitErfassung,MyUser

#@login_required
class ZeitUpdate(UpdateView):
    model = ZeitErfassung
    fields = ['beschreibung','start','ende','betreuer']
    template_name_suffix = '_update_form'


    def get_queryset(self):
    	query_set = ZeitErfassung.objects.filter(user = self.request.user)
    	return query_set



class EntferneEintrag(DeleteView):
    model = ZeitErfassung
    success_url = reverse_lazy('stundenkonto')
    


    def get_queryset(self):
    	query_set = ZeitErfassung.objects.filter(user = self.request.user)
    	return query_set


