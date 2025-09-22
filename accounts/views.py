from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = 'products:product_list'


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('products:product_list')
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('products:product_list')
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.request.user.orders.all()[:5]
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self):
        return self.request.user.profile
    
    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado exitosamente.')
        return super().form_valid(form)
