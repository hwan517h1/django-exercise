"""snulion7th URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('feeds/', include('feedpage.urls')),

]

# path('accounts/signup/', accounts.views.signup, name='signup')처럼 직접 접근하는 것도 가능함
# path('accounts/', include('django.contrib.auth.urls'))는 Django에서 제공하는 것으로 urls, view을 자동으로 처리함, template은 registration 아래 login.html을 만들어야 함
