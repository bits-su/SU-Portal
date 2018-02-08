from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all),
    path('view/(<ticket_id>\d+)/', views.view),
    path('new/', views.create),
    path('submit_ticket/', views.submit_ticket),
    path('update/(<ticket_id>\d+)/', views.update),
    path('update_ticket/(<ticket_id>\d+)/', views.update_ticket),
    path('submit_comment/(<ticket_id>\d+)/', views.submit_comment),
    path('delete/(<ticket_id>\d+)/', views.delete_ticket),
    path('delete_comment/(<comment_id>\d+)/', views.delete_comment),
    path('project/', views.project),
]
