# Generated by Django 4.0.3 on 2022-03-22 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_remove_uploaddoc_user_folder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='creater_user',
        ),
    ]
