# Generated by Django 4.1.7 on 2023-02-27 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='article',
            name='main_articl_created_b1180c_idx',
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]