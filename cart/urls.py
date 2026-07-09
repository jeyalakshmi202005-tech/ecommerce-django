from django.urls import path
from . import views

urlpatterns=[

path("",views.cart,name="cart"),

path("add/<int:id>/",views.add_to_cart,name="add"),

path("increase/<int:id>/",views.increase,name="increase"),

path("decrease/<int:id>/",views.decrease,name="decrease"),

path("remove/<int:id>/",views.remove,name="remove"),

path("checkout/", views.checkout, name="checkout"),

]