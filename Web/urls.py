from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# DAJAX, DAJAXICE
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web.views.home', name='home'),
    # url(r'^Web/', include('Web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
  #url(r'^polls/', include('polls.urls', namespace='polls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^posts/', include('posts.urls')),
  #url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
  #url(r'^djangojs/', include('djangojs.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
  )
)
