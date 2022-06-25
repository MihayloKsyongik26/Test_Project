from django.shortcuts import render
from django.http import HttpResponse
from UserAPI.models import User
from .models import Specialist

def index(request, k):
    users = User.objects.filter(specialist = k)
    specialist = Specialist.objects.filter(id = k)
    return render(request, 'UserAPI/index.html', {'users': users, 'specs': specialist})

