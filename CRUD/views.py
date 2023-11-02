from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def handlesignup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        myuser = User.objects.create_user(username=username,email=username, password=password)
        myuser.save()
    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')

        else:
            return redirect('/login')

    return render(request, "login.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        # print(name,email,age,gender)
        query = Student(name=name, email=email, password=password, gender=gender,country=country)
        query.save()
        return redirect("/")

    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        country = request.POST.get('country')

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.gender = gender
        edit.country = country
        edit.password = password
        edit.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "index.html")


def handlelogout(request):
    logout(request)
    return redirect('/signup')


from django.contrib.auth.hashers import make_password, check_password

def customlogin(request):
    if request.method == "POST":
        customemail = request.POST.get('email')
        custompassword = request.POST.get('password')
        
        # Check if a user with the given email exists in the database
        try:
            user = Student.objects.get(email=customemail)
        except Student.DoesNotExist:
            # User not found, redirect to the login page
            return redirect('/login')
        
        # Check if the entered password matches the hashed password stored in the database
        if custompassword == user.password:
            # Passwords match, perform a login action
            # You can implement your own login logic here if needed
            return redirect('/')
        else:
            # Passwords do not match, redirect to the login page
            return redirect('/login')
    
    return render(request, "customlogin.html")


