# Generated by Django 2.2 on 2020-05-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_suggested_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggested_theme',
            name='context',
            field=models.TextField(null=True),
        ),
    ]