# Generated by Django 3.2.7 on 2021-11-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20211001_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='news',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
