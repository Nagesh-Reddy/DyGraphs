from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$', views.home),    
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^design/$', views.design, name='design'),
    url(r'^profile/$', views.profile, name='profile'),
    
]