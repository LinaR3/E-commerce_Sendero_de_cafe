from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'status', 'paid', 'created_at']
    list_filter = ['paid', 'created_at', 'updated_at', 'status']
    search_fields = ['first_name', 'last_name', 'email']
    inlines = [OrderItemInline]
