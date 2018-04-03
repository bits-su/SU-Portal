from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('app/<int:user_id>/', views.show_user_info),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('aboutus/clubs/', views.clubs, name='clubs'),
    path('aboutus/depts/', views.depts, name='depts'),
    path('aboutus/techassoc/', views.techassoc, name='techassoc'),
    path('aboutus/reg/', views.reg, name='reg'),
    path('aboutus/ngos/', views.ngos, name='ngos'),
    path('calendar/', views.calendar, name='calendar'),
    path('clubs/', views.clubs, name='clubs'),
    path('aboutus/suevents/', views.suevents, name='suevents'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name="contact-us"),
    path('transport/', views.transport, name="transport"),
    path('resources/', views.resources, name="resources-us"),
    path('alumni/', views.alumni, name="alumni-connect"),
    path('resources/<str:filename>/', views.pdf_download, name = 'pdf_download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
