# Generated by Django 4.1 on 2022-09-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=100)),
                ('Image_Link', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
