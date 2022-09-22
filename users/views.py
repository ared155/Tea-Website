from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    # form=UserCreationForm()
    # return render(request, 'users/signup.html')
    if request.method == "POST":
        username = request.POST.get('username',False)
        # username=request.POST['username']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/')
        
        # if (len(username) > 20):
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('/')
        
        if password != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/')
        
        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!!")
        #     return redirect('/')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.isactive=True
        # myuser.save()
        # return redirect(reverse('users/signin/'))
        return render(request, 'users/signin.html')

    return render(request, 'users/signup.html')

def signin(request):
    # form=UserCreationForm()
    # return render(request, 'users/signin.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            first_name = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, 'users/signup.html',{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('users/signin.html')
    
    return render(request, "users/signin.html")