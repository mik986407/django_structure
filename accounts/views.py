from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#首頁
# @login_required(login_url="Login")
def index(request):
    return render(request, 'accounts/index.html')

#註冊
def sign_up(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  #重新導向到登入畫面

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

#登入
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == 'admin':
                return redirect('/shop/statistics/')  #重新導向到首頁
            else:
                return redirect('/posts/')  #重新導向到首頁
        
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def sign_in_normal(request):
    return redirect('/posts/') #重新導向到一般畫面

# 登出
def log_out(request):
    return redirect('accounts/logout.html') #重新導向到登入畫面

# 首頁
def simple_crawl(request):
    return render(request, 'accounts/index.html')