# Generated by Django 2.1.5 on 2019-01-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20190113_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterModelOptions(
            name='produtos',
            options={'verbose_name_plural': 'Produtos'},
        ),
    ]
