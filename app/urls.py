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
    path('aboutus/ngos/', views.ngos, name='ngos'),
    path('complaints/',views.complaints, name='complaints'),
    path('submit_complaint',views.submit_complaint, name='submit-complaint'),
    path('calendar/', views.calendar, name='calendar'),
    path('clubs/', views.clubs, name='clubs'),
    path('aboutus/suevents/', views.suevents, name='suevents'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name="contact-us"),
    path('transport/', views.transport, name="transport"),
    path('resources/', views.resources, name="resources-us"),
    path('alumni/', views.alumni, name="alumni-connect"),
    path('static/pdf/<str:filename>/', views.pdf_atmos, name = 'pdf_atmos'),
    path('static/pdf/<str:filename>/', views.pdf_pearl, name = 'pdf_pearl'),
    path('static/pdf/<str:filename>/', views.pdf_arena, name = 'pdf_arena'),
    path('static/pdf/<str:filename>/', views.pdf_vm, name = 'pdf_vm'),
    path('static/pdf/<str:filename>/', views.pdf_su, name = 'pdf_su')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
