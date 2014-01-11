from django.conf.urls.defaults import patterns, url
from posts import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^update/$', views.update, name='update'),
  url(r'^destroy/$', views.destroy, name='destroy'),
  #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
  #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
  #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')
)
