from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'about/index.html', {'users': users})

def user_info(request, usr_name):
    user = User.objects.filter(user_name=usr_name)[0]
    return render(request, 'about/user_info.html', {'user': user})