from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'cart_cost',
                       'total_cost', 'original_cart',
                       'stripe_pid', 'country',)

    fields = ('order_number', 'user_profile', 'date', 
              'first_name', 'last_name', 'email', 
              'phone_number', 'street_address1', 
              'street_address2', 'town_or_city', 'county', 
              'country', 'eircode', 'delivery_cost', 
              'cart_cost', 'total_cost', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'cart_cost', 
                    'delivery_cost', 'total_cost',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
