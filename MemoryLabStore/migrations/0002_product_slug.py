# Generated by Django 4.1.7 on 2023-02-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MemoryLabStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
