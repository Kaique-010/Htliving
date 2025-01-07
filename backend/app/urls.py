from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gemini_api.urls')),  # Incluir as rotas da app gemini_api
    # Aqui está o ajuste para a view do index.html
    path('', TemplateView.as_view(template_name='index.html'), name='index'), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
