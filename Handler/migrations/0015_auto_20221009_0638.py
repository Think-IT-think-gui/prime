# Generated by Django 3.2.10 on 2022-10-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0014_alter_user_info_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='Bio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Password',
            field=models.CharField(max_length=100),
        ),
    ]
