from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/feeds')
    else:
        return render(request, 'accounts/signup.html')

# 장고에서 기본적으로 제공하는 include('django.contrib.auth.urls')을 사용하면 불필요함
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/feeds')
#         else:
#             return render(request, 'accounts/login.html', {'error' : 'Username or Password is INCORRECT'})
#     else:
#         return render(request, 'accounts/login.html')

# def logout(request):
#     return render(request, 'accounts/logout.html')
