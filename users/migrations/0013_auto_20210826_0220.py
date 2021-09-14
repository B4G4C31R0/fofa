# Generated by Django 3.2.3 on 2021-08-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210802_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Link do Facebook'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='git',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Link do Git'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Link do Instagram'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Link do Linkedin'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Link do Twitter'),
        ),
    ]
