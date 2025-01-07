from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import google.generativeai as genai

from .models import Dieta
from .serializers import DietaSerializer
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Inicializa a chave da API Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))



class DietaViewSet(ModelViewSet):
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer

    @action(detail=True, methods=['post'])
    def generate_plan(self, request, pk=None):
        dieta = self.get_object()
        
        prompt_dieta = f"Crie uma dieta saudável para {dieta.name}, que tem {dieta.height} cm de altura, {dieta.weight} kg de peso, treina com frequência {dieta.train_freq}, e possui as seguintes restrições alimentares: {dieta.restrictions}."
        prompt_treino = f"Crie um plano de treino para {dieta.name}, que tem {dieta.height} cm de altura, {dieta.weight} kg de peso, treina com frequência {dieta.train_freq}, e possui as seguintes restrições: {dieta.restrictions}."

        try:
            # Chama a API Gemini para gerar a dieta e treino
            dieta_response = genai.generate_text(prompt_dieta)
            treino_response = genai.generate_text(prompt_treino)

            # Atualiza os campos diet e train do objeto Dieta
            dieta.diet = dieta_response.text.strip()  # Remove espaços extras
            dieta.train = treino_response.text.strip()  # Remove espaços extras
            dieta.save()

            # Retorna as informações geradas
            return Response(
                {
                    'dieta': dieta.diet,
                    'treino': dieta.train,
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': 'Erro ao gerar a dieta ou o treino', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GeminiPromptApiView(APIView):
    """
    View para geração de conteúdo via prompt no Gemini.
    """
    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt', '')
        model_name = request.data.get('model', 'gemini-1.5-flash')

        if not prompt:
            return Response({'error': 'Prompt é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Gerando conteúdo com o modelo especificado
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)

            return Response({'text': response.text}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': 'Erro ao chamar a API Gemini', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'