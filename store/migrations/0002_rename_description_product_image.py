# Generated by Django 3.2.18 on 2023-04-03 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='image',
        ),
    ]
