# Generated by Django 4.2.7 on 2023-11-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='summarized_text',
            field=models.TextField(default='SOME STRING'),
        ),
    ]