from django.urls import path
from .views import login_view, signup_view, home,aboutus,product_list,service

urlpatterns = [
        
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home, name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('product_list/',product_list,name='product_list'),
    path('service/',service,name='service'),
]   