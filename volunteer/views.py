from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def volunteer(request):
    return HttpResponse('You are at Volunteer page')

def register(request):
    return render(request, 'register.html')
    