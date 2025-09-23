from django.contrib import admin
from django.urls import path, include
from product.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),          
    path('products/', include('product.urls')),  
]
