from django.urls import path
from .views import login_view, signup_view, home,aboutus,service,profile,logout_view,appointment_list,uproduct_list,product_details,add_to_cart,remove_from_cart,cart,checkout,order_confirmation,payment_method,process_payment,confirm_payment


urlpatterns = [
        
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home, name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('uproduct_list/',uproduct_list,name='uproduct_list'),
    path('service/',service,name='service'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout_view'),
    path('appointments/', appointment_list, name='appointment_list'),  
    path('product/<int:id>/',product_details, name='product_details'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/', order_confirmation, name='order_confirmation'),
    path('payment-method/', payment_method, name='payment_method'),
    path('process-payment/', process_payment, name='process_payment'),
    path('confirm_payment/', confirm_payment, name='confirm_payment'),

]   