from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    # url(r'^$', views.add, name='add'),
    url(r'^$', views.index, name='index'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<user_id>\d+)/delete/$', views.delete, name='delete')
    # url(r'^$', views.index, name='index'),
    # url(r'^add/$', views.add, name='add'),
    # url(r'^edit/$', views.edit, name='edit'),
]
