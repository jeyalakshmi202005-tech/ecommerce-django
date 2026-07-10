from django.shortcuts import render, redirect
from orders.models import Order

def home(request):
    return render(request, "home.html")

def checkout(request):
    cart_items = request.session.get("cart", [])

    for item in cart_items:
        Order.objects.create(
            product_id=item["id"],
            quantity=item["quantity"]
        )

    request.session["cart"] = []

    return render(request, "success.html")