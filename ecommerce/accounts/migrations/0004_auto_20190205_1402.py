# Generated by Django 2.1.5 on 2019-02-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_endereco_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18),
        ),
    ]
