# Generated by Django 2.2.10 on 2020-09-02 23:17

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=120, verbose_name='Nome Cliente')),
                ('documento', models.CharField(max_length=25, verbose_name='CPF ou CNPJ')),
                ('cep', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=120)),
                ('numero', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcionario', models.CharField(max_length=120, verbose_name='Nome Funcionário')),
                ('cep', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=120)),
                ('numero', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('tipo_servico', models.CharField(max_length=50, verbose_name='Tipo do Serviço')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_eq', models.CharField(max_length=100, verbose_name='Nome do Equipamento')),
                ('fornecedor', models.CharField(max_length=100)),
                ('valor_compra', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Valor de Custo')),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Valor de Venda')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Grupo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Marca')),
            ],
        ),
    ]
