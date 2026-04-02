from django.shortcuts import render,redirect
from form.models import information
# Create your views here.
def form_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, email, age, gender)

        data = information(name=name,email=email,age=age,gender=gender)
        data.save()
    return render(request, 'form.html')