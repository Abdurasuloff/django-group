# Generated by Django 4.1.7 on 2023-02-27 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('can_view_author', 'Can View Article Author')]},
        ),
    ]
