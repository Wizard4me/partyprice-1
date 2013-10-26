# coding=UTF-8

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from dajaxice.core import dajaxice_autodiscover#, dajaxice_config
dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    #url(r'^', include('party_bl.urls')),
    #url(r'^', 'party_bl.views.index'),

    # Examples:
    # url(r'^$', 'partyprice.views.home', name='home'),
    # url(r'^partyprice/', include('partyprice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'', 'party_bl.views.index')
    #url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()