from django.conf.urls import url

from . import views

app_name ='servers'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^servers1c$', views.servers1c, name='servers1c'),
    url(r'^new_server1c$', views.new_server1c, name='new_server1c'),
]
