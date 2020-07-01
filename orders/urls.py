from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'orders'
urlpatterns = [

	path('', views.checkout, name='checkout'),
	path('orders/', views.orders, name='orders'),

	

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)