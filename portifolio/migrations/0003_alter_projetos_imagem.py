# Generated by Django 4.2.6 on 2023-10-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0002_projetos_projetostags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='imagem',
            field=models.ImageField(upload_to='portifolio/projetos'),
        ),
    ]