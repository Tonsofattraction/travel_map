from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^travel_map/$', 'travel_map.views.home', name='home'),
    url(r'^travel_map/get_data$', 'travel_map.views.get_data'),
    url(r'^travel_map/visit', 'travel_map.views.visit'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
