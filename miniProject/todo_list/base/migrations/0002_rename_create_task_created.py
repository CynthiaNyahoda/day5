# Generated by Django 4.1.7 on 2023-03-12 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='create',
            new_name='created',
        ),
    ]
