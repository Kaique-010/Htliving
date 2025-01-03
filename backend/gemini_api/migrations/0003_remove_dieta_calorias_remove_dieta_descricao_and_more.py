# Generated by Django 5.1.4 on 2025-01-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemini_api', '0002_dieta_prompt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dieta',
            name='calorias',
        ),
        migrations.RemoveField(
            model_name='dieta',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='dieta',
            name='nome',
        ),
        migrations.AddField(
            model_name='dieta',
            name='height',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Altura (em cm)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dieta',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dieta',
            name='restrictions',
            field=models.TextField(blank=True, verbose_name='Restrições Alimentares'),
        ),
        migrations.AddField(
            model_name='dieta',
            name='train_freq',
            field=models.CharField(choices=[('low', 'Baixa (1-2 vezes por semana)'), ('medium', 'Média (3-4 vezes por semana)'), ('high', 'Alta (5 ou mais vezes por semana)')], default=1, max_length=50, verbose_name='Frequência de Treino'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dieta',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Peso (em kg)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dieta',
            name='prompt',
            field=models.TextField(verbose_name='Prompt para a API Gemini'),
        ),
    ]
