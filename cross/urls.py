from django.urls import path, include
from . import views

urlpatterns = [

	path('',views.cross_main, name='main'),
	path('russian/',views.main2, name='russian'),

]