# Generated by Django 4.2.7 on 2023-12-03 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_audio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
