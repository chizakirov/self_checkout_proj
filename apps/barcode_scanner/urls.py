from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'upload$', views.upload_code),
    url(r'read$', views.read_barcode),
    url(r'live$', views.scanner),
    url(r'display/(?P<id>\d+)$', views.display_page),
]
