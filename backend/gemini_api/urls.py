# gemini_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DietaViewSet, GeminiPromptApiView

# Cria um roteador e registra a viewset DietaViewSet
router = DefaultRouter()
router.register(r'dietas', DietaViewSet, basename='dieta')

urlpatterns = [
    # Incluir as URLs do router (para DietaViewSet)
    path('dietas/', include(router.urls)),

    # URL específica para a ação generate_plan
    path('dietas/<int:pk>/generate_plan/', DietaViewSet.as_view({'post': 'generate_plan'}), name='generate-plan'),

    # URL para a view GeminiPromptApiView
    path('gemini-prompt/', GeminiPromptApiView.as_view(), name='gemini-prompt'),
]
