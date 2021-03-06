# Generated by Django 3.1.7 on 2022-02-24 10:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20220224_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(blank='true', null='True')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=20)),
                ('text', ckeditor.fields.RichTextField(blank='true', null='True')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=30)),
                ('text', ckeditor.fields.RichTextField(blank='true', null='True')),
            ],
        ),
    ]
