# Generated by Django 4.2.7 on 2023-12-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('name', models.AutoField(primary_key=True, serialize=False)),
                ('audio_data', models.BinaryField()),
            ],
        ),
    ]