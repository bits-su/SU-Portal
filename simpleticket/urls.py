from django.conf.urls import include
from django.urls import path
from simpleticket import views

urlpatterns = [
    path('', views.view_all),
    path('view/<int:ticket_id>/', views.view),
    path('new/', views.create),
    path('submit_ticket/', views.submit_ticket),
    path('update/<int:ticket_id>/', views.update),
    path('update_ticket/<int:ticket_id>/', views.update_ticket),
    path('submit_comment/<int:ticket_id>/', views.submit_comment),
    path('delete/(<int:ticket_id>\d+)/', views.delete_ticket),
    path('delete_comment/<int:comment_id>/', views.delete_comment),
    # path('project/', views.project),
]
