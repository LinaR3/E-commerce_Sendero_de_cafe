from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.contrib import messages
from django.urls import reverse_lazy
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'
    success_url = reverse_lazy('orders:order_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
    
    def form_valid(self, form):
        cart = Cart(self.request)
        if len(cart) == 0:
            messages.error(self.request, 'Tu carrito está vacío.')
            return redirect('cart:cart_detail')
        
        order = form.save(commit=False)
        order.user = self.request.user
        order.total_amount = cart.get_total_price()
        order.save()
        
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        
        cart.clear()
        messages.success(self.request, f'Pedido #{order.id} creado exitosamente.')
        return redirect('orders:order_detail', order_id=order.id)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
