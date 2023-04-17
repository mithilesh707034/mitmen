from django.shortcuts import render
from .models import Contact
def home(Request):
    return render (Request,'home.html')

def about(Request):
    return render (Request,'about.html')

def contact(Request):
    if Request.method=="POST":
        c=Contact()
        c.name=Request.POST.get('name')
        c.email=Request.POST.get('email')
        c.phone=Request.POST.get('phone')
        c.subject=Request.POST.get('subject')
        c.message=Request.POST.get('message')
        c.save()
    return render (Request,'contact.html')

def ai(Request):
    return render (Request,'ai.html')

def webDevelopment(Request):
    return render(Request,'web-development.html')

def digitalMarketing(Request):
    return render(Request,'digital-marketing.html')
