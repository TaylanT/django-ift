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
from django.conf.urls import url,include
#beispiel
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
import login.views
import stundenkonto.views
from login.forms import MyCustomUserForm

from aenderung.views import ZeitUpdate


urlpatterns = [


    url(r'^admin/', admin.site.urls),
    # url(r'^login/$','login.views.login',name='login'),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
    ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'login.views.home',name="home"),
    url(r'^stundenkonto/$', stundenkonto.views.ubersicht,name="stundenkonto"),
    url(r'^status/$', stundenkonto.views.status,name="status"),
    url(r'^thanks/$', stundenkonto.views.thanks,name="thanks"),
    #url(r'^profile/$', login.views.profilesi,name="profile"),
     url(r'accounts/profile/zeiterfassung/(?P<pk>[0-9]+)/$', ZeitUpdate.as_view(), name='zeit-update')


]
