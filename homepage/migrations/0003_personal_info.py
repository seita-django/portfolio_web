# Generated by Django 3.1.7 on 2022-02-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Profession', models.CharField(max_length=30)),
                ('Email_Address', models.CharField(max_length=20)),
                ('Phone_Number', models.CharField(max_length=20)),
            ],
        ),
    ]
