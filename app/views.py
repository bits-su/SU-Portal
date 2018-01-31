from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.http import HttpResponse

@login_required
def index(request):
    user_email = request.user.email
    if(not user_email.endswith('hyderabad.bits-pilani.ac.in')):
        logout(request)
        User.objects.filter(email=user_email).delete()
        return index(request)
    else:
        return HttpResponse("Hello, " + request.user.username)


def home(request):
    return render(request,'home.html')

def show_user_info(request, user_id):
    # Sample view. Renders template to display user details.
    # Create new user from admin portal /admin/
    # Browse /app/<user_id>
    user = User.objects.get(id=user_id)
    return render(request, 'sample_template.html', {'user':user})
