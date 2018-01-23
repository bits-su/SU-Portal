from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app/<int:user_id>/', views.show_user_info),
]
