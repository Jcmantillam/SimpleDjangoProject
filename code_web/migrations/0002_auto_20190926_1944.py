# Generated by Django 2.2.4 on 2019-09-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_web', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='usuarios_registrados',
            index=models.Index(fields=['nombre'], name='code_web_us_nombre_d02001_idx'),
        ),
        migrations.AddIndex(
            model_name='usuarios_registrados',
            index=models.Index(fields=['email'], name='code_web_us_email_5e0d12_idx'),
        ),
    ]
