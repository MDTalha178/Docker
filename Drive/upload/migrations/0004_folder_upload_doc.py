# Generated by Django 4.0.3 on 2022-03-10 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='upload_doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upload_doc', to='upload.uploaddoc'),
        ),
    ]
