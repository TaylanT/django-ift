from django.shortcuts import render, HttpResponseRedirect
from .models import SignUp, ZeitErfassung
from .forms import SignUpForm, ZeitForm

# Create your views here.

def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
	    	save_it=form.save(commit=False)
	    	save_it.save()


	        # process the data in form.cleaned_data as required
	        # ...
	        # redirect to a new URL:
	        return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def home(request):

	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
	    form = ZeitForm(request.POST)
	    # check whether it's valid:
	    if form.is_valid():
	    	save_it=form.save(commit=False)
	    	save_it.user=request.user
	    	save_it.dt=save_it.ende-save_it.start
	    	save_it.save()


	        # process the data in form.cleaned_data as required
	        # ...
	        # redirect to a new URL:
	        return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
	    form = ZeitForm

	return render(request, 'home.html', {'form': form})

def danke(request):
	#zt=ZeitErfassung.objects.all()
	zt=ZeitErfassung.objects.filter(user__username=request.user)

	return render(request,'secondpage.html',{'zt':zt})
   

    