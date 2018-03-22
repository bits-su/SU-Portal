from django.shortcuts import render
from .models import User, Complaint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django import forms
from django.urls import reverse
from django.contrib import messages

from .forms import ComplaintForm
from wsgiref.util import FileWrapper
import os

def home(request):
    if(request.user.is_authenticated):
        user_email = request.user.email
        if(not user_email.endswith('hyderabad.bits-pilani.ac.in')):
            logout(request)
            User.objects.filter(email=user_email).delete()
            messages.warning(request, 'Login Failed. Invalid email.')
            return HttpResponseRedirect(reverse('login'))
        else:
            pass
    return render(request,'home.html')

def show_user_info(request, user_id):
    # Sample view. Renders template to display user details.
    # Create new user from admin portal /admin/
    # Browse /app/<user_id>
    user = User.objects.get(id=user_id)
    return render(request, 'sample_template.html', {'user':user})

def contact(request):
	#user = User.objects.get(id=user_id)
	context = RequestContext(request)
	contact_list = User.objects.filter(groups__name='SU Council')
	context_dict = {'members': contact_list}
	return render(request, 'contact.html', context_dict, context)

def calendar(request):
    return render(request, 'calendar.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def clubs(request):
    return render(request, 'clubs.html')

def depts(request):
    return render(request, 'depts.html')

def techassoc(request):
    return render(request, 'techassoc.html')

def ngos(request):
    return render(request, 'ngos.html')

def suevents(request):
    return render(request, 'suevents.html')

def alumni(request):
    return render(request, 'alumni.html')

def logout_view(request):
    logout(request)
    return home(request)

def resources(request):
    return render(request, 'resources.html')

def transport(request):
    return render(request, 'transport.html')

def pdf_atmos(request, filename):
    path = os.path.abspath('/static/pdf/')
    f = open(path+filename, "rb")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=atmos.pdf'
    f.close()
    return response

def pdf_pearl(request, filename):
    path = os.path.abspath('/static/pdf/')
    f = open(path+filename, "rb")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=pearl.pdf'
    f.close()
    return response

def pdf_arena(request, filename):
    path = os.path.abspath('/static/pdf/')
    f = open(path+filename, "rb")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=arena.pdf'
    f.close()
    return response

def pdf_vm(request, filename):
    path = os.path.abspath('/static/pdf/')
    f = open(path+filename, "rb")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=vm.pdf'
    f.close()
    return response

def pdf_su(request, filename):
    path = os.path.abspath('/static/pdf/')
    f = open(path+filename, "rb")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=su.pdf'
    f.close()
    return response
