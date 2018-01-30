from django.shortcuts import render
from .models import User

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")


def home(request):
    return render(request,'home.html')

def show_user_info(request, user_id):
    # Sample view. Renders template to display user details.
    # Create new user from admin portal /admin/
    # Browse /app/<user_id>
    user = User.objects.get(id=user_id)
    return render(request, 'sample_template.html', {'user':user})
