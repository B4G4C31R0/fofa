# Generated by Django 3.2.3 on 2021-07-30 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_membro_lider_objetivo'),
        ('swot', '0022_auto_20210729_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatores',
            name='criador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.membro'),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='criador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.membro'),
        ),
    ]