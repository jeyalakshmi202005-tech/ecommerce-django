from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product

def cart(request):
    items = Cart.objects.all()

    total = 0

    for item in items:
        total += item.product.price * item.quantity

    return render(request,"cart.html",{
        "items":items,
        "total":total
    })

def add_to_cart(request,id):
    product = get_object_or_404(Product,id=id)

    item,created = Cart.objects.get_or_create(product=product)

    if not created:
        item.quantity +=1
        item.save()

    return redirect("cart")

def increase(request,id):
    item=get_object_or_404(Cart,id=id)
    item.quantity +=1
    item.save()
    return redirect("cart")

def decrease(request,id):
    item=get_object_or_404(Cart,id=id)

    if item.quantity>1:
        item.quantity-=1
        item.save()
    else:
        item.delete()

    return redirect("cart")

def remove(request,id):
    item=get_object_or_404(Cart,id=id)
    item.delete()
    return redirect("cart")
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Cart
from orders.models import Order

def checkout(request):
    cart_items = Cart.objects.all()

    for item in cart_items:
        Order.objects.create(
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity
        )

    cart_items.delete()

    messages.success(request, "🎉 Order Successfully Placed!")

    return render(request, "success.html")
