from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),	
    path('app/<int:user_id>/', views.show_user_info),
]
