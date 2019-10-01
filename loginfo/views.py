from django.shortcuts import render
from .models import Customer

# Create your views here.


def info(request):
    return render(request, 'loginfo/info.html')


def userlist(request):
    users = Customer.objects.all()
    return render(request, 'loginfo/info.html', {'users': users})
