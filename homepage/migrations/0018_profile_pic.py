# Generated by Django 3.1.7 on 2022-02-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_social_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='profile')),
            ],
        ),
    ]
