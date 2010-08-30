from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib.auth.views import login, logout, logout_then_login, password_change
from larpsite.views import register

  
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
  
urlpatterns = patterns('',
    # Example:
#    (r'^larpsite/', include('larpsite.foo.urls')),
  
    (r'^admin/', include(admin.site.urls)),
  
#    (r'^', include('larpsite.mainpages.urls')),
    (r'^', include('larpsite.eventCRUD.urls')),
  
    (r'^ec/', include('larpsite.eventCRUD.urls')),
    (r'^users/', include('larpsite.eventCRUD.urls')),
    (r'^people/', include('larpsite.eventCRUD.urls')),
#   (r'^games/', include('larpsite.eventCRUD.urls')),
  
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
  
#   (r'^search/', include('haystack.urls')),
#    (r'^search/', include('search.urls')),
  
    (r'^accounts/', include('registration.urls')),
       
    (r'^comments/', include('django.contrib.comments.urls')),
  
    (r'^contact/', include('contact_form.urls')),
     
    (r'^messages/', include('messages.urls')),
     
#   (r'^blog/', include('basic.blog.urls')),    
     
    (r'^notification/', include('notification.urls')),  
  
)