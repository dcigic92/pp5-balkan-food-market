from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    cart_cost = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        cart_cost += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if cart_cost < settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = settings.STANDARD_DELIVERY
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - cart_cost
    else:
        delivery_cost = 0
        free_delivery_delta = 0
    
    total_cost = delivery_cost + cart_cost
    
    context = {
        'cart_items': cart_items,
        'cart_cost': cart_cost,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total_cost': total_cost,
    }

    return context