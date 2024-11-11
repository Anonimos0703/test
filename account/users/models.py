from django.contrib.auth.models import AbstractUser
from django.db import models
from admin_page.models import Product

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.username
    
class Order(models.Model):
    PAYMENT_METHODS = [
        ('GCash', 'GCash'),
        ('PayPal', 'PayPal'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    
class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_price(self):
        return self.quantity * self.product.price
