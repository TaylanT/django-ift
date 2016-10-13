from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import datetime
from django.shortcuts import HttpResponseRedirect
from login.models import ZeitErfassung


# @login_required
class ZeitUpdate(UpdateView):
    model = ZeitErfassung
    fields = ['beschreibung', 'start', 'ende', 'betreuer']
    template_name_suffix = '_update_form'

    def get_queryset(self):
        query_set = ZeitErfassung.objects.filter(user=self.request.user)
        return query_set

    def form_valid(self, form):
        save_it = form.save(commit=False)
        save_it.user = self.request.user
        save_it.dt = save_it.ende - save_it.start
        save_it.save()
        return HttpResponseRedirect('/thanks/')



class EntferneEintrag(DeleteView):
    model = ZeitErfassung
    success_url = reverse_lazy('stundenkonto', kwargs={'monat':datetime.date.today().month})

    def get_queryset(self):
        query_set = ZeitErfassung.objects.filter(user=self.request.user)
        return query_set
