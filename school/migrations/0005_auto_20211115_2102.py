# Generated by Django 3.2.7 on 2021-11-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_slides'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slides',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='slides',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='slides'),
        ),
        migrations.AddField(
            model_name='slides',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='slides'),
        ),
    ]
