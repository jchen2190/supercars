# Generated by Django 4.2.1 on 2023-05-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supercars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
