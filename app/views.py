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


from .models import User

from .models import User

from .forms import ComplaintForm


@login_required
def home(request):
    user_email = request.user.email
    if(not user_email.endswith('hyderabad.bits-pilani.ac.in')):
        logout(request)
        User.objects.filter(email=user_email).delete()
        return home(request)
    else:
        return render(request,'home.html')
    # return render(request,'home.html')


def home(request):
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
	contact_list = User.objects.filter(is_staff=True)
	context_dict = {'members': contact_list}
	return render(request, 'contact.html', context_dict, context)

def complaints(request):

    complaints_form = ComplaintForm()
    context = {
        'form' : complaints_form,
    }
    return render(request,'complaints-express.html',context)

@login_required
def submit_complaint(request):

    if request.user.is_authenticated:
        user = User.objects.get(id=request.session['_auth_user_id'])

        form = ComplaintForm(request.POST)
        if form.is_valid:
            title = form["title"].value()
            complaint_text = form["complaint"].value()

        complaint = Complaint.objects.create(
                        title=title,
                        complaint=complaint_text,
                        uploadedby=user,
                        )

        return HttpResponse("Submitted")
    else:
        return HttpResponse("login plis")

def calendar(request):
    return render(request, 'calendar.html')
