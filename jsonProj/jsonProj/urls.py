from django.conf.urls import patterns, include, url
from jsonProj.views import getJSON
from jsonProj.views import getHeadlines

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jsonProj.views.home', name='home'),
    # url(r'^jsonProj/', include('jsonProj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^json/full$', getJSON),
    url(r'^json/headlines$', getHeadlines),
)
