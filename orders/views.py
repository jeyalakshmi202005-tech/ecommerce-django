from django.shortcuts import render
from .models import Order

def my_orders(request):
    orders = Order.objects.all().order_by("-ordered_at")
    return render(request, "orders.html", {"orders": orders})