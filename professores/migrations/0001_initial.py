# Generated by Django 4.1.1 on 2022-09-13 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ativo', models.BooleanField()),
                ('formacao', models.CharField(blank=True, max_length=255, null=True)),
                ('especialidade', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
