from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_view(request):
  
    
    if request.method == 'POST':
        u_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_confirm')

        if not u_name or not pass1:
            messages.error(request, "Hamma maydonlarni to'ldiring!")
        elif pass1 != pass2:
            messages.error(request, "Parollar bir-biriga mos kelmadi!")
        elif User.objects.filter(username=u_name).exists():
            messages.error(request, "Bu foydalanuvchi nomi band!")
        else:
            user = User.objects.create_user(username=u_name, password=pass1)
            auth_login(request, user)
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect('product_list')
            
    return render(request, 'auth/register.html')

@csrf_exempt
def login_view(request):
 
    
    if request.method == 'POST':
        u_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        
        user = authenticate(request, username=u_name, password=pass1)
        
        if user is not None:
            auth_login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Username yoki parol xato!")
            
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all() 
    return render(request, 'shop/product_list.html', {'products': products})

@login_required(login_url='login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})
