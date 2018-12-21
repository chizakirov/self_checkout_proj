from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from apps.barcode_scanner.models import *

urlpatterns = [
    url(r'order$', views.process_order),
    url(r'order_review$', views.order_review),
    url(r'delete/(?P<id>\d+)$', views.delete),
    url(r'checkout$', views.checkout_process),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)