"""jetzt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include


from django.contrib import admin
# from registration.backends.simple.views import RegistrationView
from login.views import EigeneRegistration, login, home
from stundenkonto.views import UebersichView, status, thanks
from login.forms import MyCustomUserForm

from aenderung.views import ZeitUpdate, EntferneEintrag
from django.contrib.auth.decorators import login_required


urlpatterns = [


    url(r'^admin/', admin.site.urls),
    url(r'^recover/', include('password_reset.urls')),
    # url(r'^login/$','login.views.login',name='login'),
    # url(r'^accounts/register/$',
    #     RegistrationView.as_view(
    #         form_class=MyCustomUserForm
    #     ),
    #     name='registration_register'),
    url(r'^accounts/register/$',
        EigeneRegistration.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', home, name="home"),
    url(r'^stundenkonto/$', UebersichView.as_view(), name="stundenkonto"),
    url(r'^stundenkonto/(?P<monat>[0-9]+)/$', UebersichView.as_view(), name="stundenkonto"),
    url(r'^status/$', status, name="status"),
    url(r'^status/(?P<monat>[0-9]+)/$', status, name="status"),
    url(r'^thanks/$', thanks, name="thanks"), 
    # url(r'^profile/$', login.views.profilesi,name="profile"),

    url(r'zeiterfassung/(?P<pk>[0-9]+)/$',
        login_required(ZeitUpdate.as_view()),
        name='zeit-update'),

    url(r'zeiterfassung/delete/(?P<pk>[0-9]+)/$',
        login_required(EntferneEintrag.as_view()),
        name='zeit-delete')



]
