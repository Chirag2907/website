from django.shortcuts import render
from home.models import contacts

# Create your views here.
def home(request):
    context = {
        'name':'chirag', 'course':'django'
    }
    return render(request, 'home.html', context) #render a html page
    # return HttpResponse("this is my home page") #use this to directly print something

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        details = request.POST['details']
        contact = contacts(name=name, email=email, details=details)
        contact.save()
        print("Data has been written in the DataBase!")
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')
