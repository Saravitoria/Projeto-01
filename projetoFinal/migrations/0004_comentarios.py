# Generated by Django 4.2.6 on 2023-11-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoFinal', '0003_alter_filme_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=80)),
                ('comentario', models.TextField()),
            ],
        ),
    ]
