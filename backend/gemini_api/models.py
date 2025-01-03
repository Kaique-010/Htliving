from django.db import models

class Dieta(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Altura (em cm)")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (em kg)")
    train_freq = models.CharField(
        max_length=50,
        choices=[
            ('low', 'Baixa (1-2 vezes por semana)'),
            ('medium', 'Média (3-4 vezes por semana)'),
            ('high', 'Alta (5 ou mais vezes por semana)')
        ],
        verbose_name="Frequência de Treino"
    )
    restrictions = models.TextField(blank=True, verbose_name="Restrições Alimentares")
    prompt = models.TextField(verbose_name="Prompt para a API Gemini")
    diet = models.TextField(verbose_name="Criar Dieta")
    train = models.TextField(verbose_name="Modelo de Treino")

    def __str__(self):
        return self.name
