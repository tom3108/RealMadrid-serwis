from django.urls import path
from . import views

urlpatterns = [
	path('',views.art_list, name='art_list'),
	path('art/<int:pk>/', views.art_detail, name='art_detail'),
	]