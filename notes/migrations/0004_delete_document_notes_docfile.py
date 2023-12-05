# Generated by Django 4.2.7 on 2023-12-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='notes',
            name='docfile',
            field=models.FileField(default='SOME STRING', upload_to='documents/%Y/%m/%d'),
        ),
    ]