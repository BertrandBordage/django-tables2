# coding: utf-8
from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('example.app.views',
    url(r'^$',             'multiple'),
    url(r'^class-based/$', 'class_based'),
    url(r'^tutorial/$',    'tutorial'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
