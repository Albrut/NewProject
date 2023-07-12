from django.urls import path, include
from . import views

urlpatterns = [

	path('',views.cross_main, name='cross_1'),
	path('main/',views.cross_main,name='cross_1'),
    path('about/',views.about,name='about'),
	path('sneakers/', views.sneakers_view,name='sneakers'),
	path('add_sneakers/', views.add_sneakers_view, name = 'add'),
	path('products/',views.product,name='products'),
	path('contact/',views.contact,name='contact'),
	path('moreinf1/',views.more_inf1,name='more_inf1'),
	path('moreinf2/',views.more_inf2,name='more_inf1'),
	path('moreinf3/',views.more_inf3,name='more_inf1'),
	path('moreinf4/',views.more_inf4,name='more_inf1'),
	path('moreinf5/',views.more_inf5,name='more_inf1'),
	path('moreinf6/',views.more_inf6,name='more_inf1'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('reg/',views.reg,name='reg'),
	path('home/',views.cross_main,name='cross_1'),

]