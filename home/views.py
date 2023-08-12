from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your request is submited successfully. Thank you!")

    return render(request, 'contact.html')
# Create your views here.
def vanilla(request):
    return render(request, 'vanilla.html')

def chocolate(request):
    return render(request, 'chocolate.html')

def strawberry(request):
    return render(request, 'strawberry.html')