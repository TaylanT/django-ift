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
import login.views
import stundenkonto.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$','login.views.login',name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'login.views.home',name="home"),
    url(r'^stundenkonto/$', stundenkonto.views.ubersicht,name="stundenkonto"),
    url(r'^status/$', stundenkonto.views.status,name="status"),
    url(r'^profile/$', login.views.profilesi,name="profile"),


]
