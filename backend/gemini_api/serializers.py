from rest_framework import serializers
from .models import Dieta

class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = '__all__'
        
    diet = serializers.CharField(read_only=True)
    train = serializers.CharField(read_only=True)
    prompt = serializers.CharField(read_only=True)

    def validate_altura(self, value):
        if value <= 0:
            raise serializers.ValidationError("A altura deve ser maior que 0.")
        return value

    def validate_peso(self, value):
        if value <= 0:
            raise serializers.ValidationError("O peso deve ser maior que 0.")
        return value

    def validate_frequencia_treino(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("A frequência de treino deve ser um número.")
        return value

class PromptSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=500)