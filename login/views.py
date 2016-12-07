from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ZeitForm
from datetime import datetime
from registration.backends.hmac.views import RegistrationView
from stundenkonto.models import StatusUebersicht

# Create your views here.


class EigeneRegistration(RegistrationView):

    
    def get_success_url(self, user):
        o = StatusUebersicht(User=user, Monat=datetime.now().month)
        o.save()
        return 'registration_complete'



def home(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ZeitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.user = request.user
            # save_it.dt = save_it.ende - save_it.start
            save_it.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ZeitForm

    return render(request, 'home.html', {'form': form})
