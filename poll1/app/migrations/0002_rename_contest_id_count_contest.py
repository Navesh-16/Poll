# Generated by Django 4.1.5 on 2024-04-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='count',
            old_name='contest_id',
            new_name='contest',
        ),
    ]
