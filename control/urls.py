from django.urls import path
from . import views

app_name = 'control'
urlpatterns = [
	path('', views.index, name='index'),
	path('silent', views.silent, name='silent'),
	path('<str:dir>', views.dir, name='dir')
]