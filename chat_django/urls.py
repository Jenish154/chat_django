"""chat_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings

routes = getattr(settings, 'REACT_ROUTES', [])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls'), name='api-auth'),
    path('api/', include('api.urls')),
    path('', login_required(TemplateView.as_view(template_name='index.html')), name='chat'),
    path('search/<str:name>', login_required(TemplateView.as_view(template_name='index.html'))),
    path('chat/<str:name>', login_required(TemplateView.as_view(template_name='index.html'))),

]

