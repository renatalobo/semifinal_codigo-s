# Generated by Django 4.0.6 on 2022-07-16 22:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('tipo', models.CharField(choices=[('PF', 'Fisica'), ('PJ', 'Juridica')], default='PF', max_length=2)),
                ('cpf_cnpj', models.CharField(max_length=14, null=True, unique=True)),
                ('endereco', models.CharField(max_length=100, null=True)),
                ('telefone', models.CharField(max_length=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta_origem', models.CharField(max_length=20)),
                ('conta_destino', models.CharField(max_length=20)),
                ('data_transacao', models.DateField(default=datetime.date.today)),
                ('valor', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Transações',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.CharField(max_length=20, null=True, unique=True)),
                ('deposito_inicial', models.FloatField(default=0, null=True)),
                ('data_abertura', models.DateField(default=datetime.date.today)),
                ('saldo_conta', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_digital.cliente')),
            ],
        ),
    ]
