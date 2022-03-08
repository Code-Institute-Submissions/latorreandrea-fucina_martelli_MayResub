from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('order_number', 'full_name', 'phone_number', 
              'email_address', 'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county', 
              'date', 'order_status', 'order_total',)

    list_display = ('order_number', 'full_name', 'date', 'order_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)