from django.conf.urls import url
from django.contrib.auth.views import login, logout 

from . import views

app_name ='users'

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': "/"}, name='logout'),
]