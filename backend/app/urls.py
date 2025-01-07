# backend/urls.py
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gemini_api.urls')),  # Incluir as rotas da app gemini_api
    path('', TemplateView.as_view(template_name='index.html')),
]
