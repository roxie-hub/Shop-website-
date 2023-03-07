from django.http.response import JsonResponse
from django.shortcuts import render

from cart.cart import Cart

from .models import Order, OrderItem


def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        name = request.user.user_name
        carttotal = cart.get_total_price()

        order = Order.objects.create(user_id=user_id, full_name=name, total_paid=carttotal)
        order_id = order.pk

        for item in cart:
            OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])
        cart.clear()
        response = JsonResponse({'success': 'Return something'})
        return response


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    return orders