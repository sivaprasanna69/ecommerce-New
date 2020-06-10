from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'products'
urlpatterns = [

	path('', views.home, name='index'),

	path('s/', views.search, name='search'),

	path('all/', views.all, name='all'),

	path('<slug:slug>/',views.single, name='single_product'),


	
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)