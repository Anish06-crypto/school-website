# Generated by Django 3.2.7 on 2021-11-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20211115_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slides1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='slides')),
            ],
        ),
        migrations.CreateModel(
            name='Slides2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='slides')),
            ],
        ),
        migrations.CreateModel(
            name='Slides3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='slides')),
            ],
        ),
        migrations.DeleteModel(
            name='Slides',
        ),
    ]
