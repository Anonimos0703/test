# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login
        

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
            
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    storage = messages.get_messages(request)
    for message in storage:
        pass
    storage.used = True
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def aboutus(request):
    return render(request, 'users/aboutus.html')

def product_list(request):
    products = [
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
    ]
    return render(request, 'users/product_list.html',{'products': products})

def service(request):
    return render(request, 'users/service.html')




def home(request):
    products = [
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
        
        
    ]
    return render(request, 'users/home.html',{'products': products})  # Ensure you have a template named 'home.html'

