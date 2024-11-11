# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from appointment.models import Appointment
from admin_page.models import Product
from django.shortcuts import render, get_object_or_404
from .models import CartItem
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem, Order

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
 

def logout_view(request):
    logout(request)
    return redirect('login')


def aboutus(request):
    return render(request, 'users/aboutus.html')

def uproduct_list(request):
    products = Product.objects.only('name', 'price', 'image') 
    return render(request, 'users/uproduct_list.html',{'products': products})

def service(request):
    return render(request, 'users/service.html')

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'users/product_details.html', {'product': product})

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if request.user.is_authenticated:      
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
        else:      
            if 'cart' not in request.session:
                request.session['cart'] = {}
            if str(id) in request.session['cart']:
                request.session['cart'][str(id)] += quantity
            else:
                request.session['cart'][str(id)] = quantity
            request.session.modified = True
        return redirect('cart')

def cart(request):
    cart_items = []
    total = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.get_total_price() for item in cart_items)
    else:
        if 'cart' in request.session:
            cart = request.session['cart']
            for product_id, quantity in cart.items():
                product = get_object_or_404(Product, id=product_id)
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': quantity * product.price,
                })
                total += quantity * product.price

    return render(request, 'users/cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request,id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, user=request.user, product__id=id)
        cart_item.delete()
    else:
        if 'cart' in request.session:
            cart = request.session['cart']
            if str(id) in cart:
                del cart[str(id)]
                request.session.modified = True

    return redirect('cart')



def home(request):
    products = [
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Cat Food', 'price': 200, 'image': 'cat_food.jpg'},
        {'name': 'Dog Food', 'price': 180, 'image': 'dog_food.jpg'},  
        
        
    ]
    return render(request, 'users/home.html',{'products': products})  



@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        pass
    
    context = {
        'user': user,
    }
    return render(request, 'users/profile.html', context)

def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'users/appointment_schedule.html', {'appointments': appointments})


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        cart_items.delete()
        return redirect('order_confirmation')

    return render(request, 'users/checkout.html', {'cart_items': cart_items, 'total': total})
    
def order_confirmation(request):
    return render(request, 'users/order_confirmation.html')

@login_required
def payment_method(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':            
        request.session['cart_total'] = str(total)
        return render(request, 'users/payment_method.html', {'cart_items': cart_items, 'total': total})

    return redirect('cart')

@login_required
def process_payment(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.get_total_price() for item in cart_items)

        if not cart_items:
            messages.error(request, 'Your cart is empty.')
            return redirect('cart')

        try:
            order = Order.objects.create(
                user=request.user,
                total_amount=total,
                payment_method=payment_method.capitalize(),
                status='Pending'
            )

            for cart_item in cart_items:
                cart_item.order = order
                cart_item.save()

            cart_items.delete()

            if 'cart' in request.session:
                del request.session['cart']
                request.session.modified = True

            if payment_method == 'gcash':
                messages.success(request, 'Order placed successfully! Proceeding with GCash payment...')
            elif payment_method == 'paypal':
                messages.success(request, 'Order placed successfully! Redirecting to PayPal...')

            return redirect('order_confirmation')

        except Exception as e:
            messages.error(request, f'An error occurred while processing your order: {str(e)}')
            return redirect('cart')

    return redirect('payment_method')


def confirm_payment(request):
    return render(request, 'order_confirmation.html')



