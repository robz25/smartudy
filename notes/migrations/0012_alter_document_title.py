# Generated by Django 4.2.7 on 2023-12-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_document_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default='No title provided', max_length=255),
        ),
    ]
