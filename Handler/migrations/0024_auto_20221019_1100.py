# Generated by Django 3.2.10 on 2022-10-19 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0023_auto_20221019_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_list',
            name='Idd_Id',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_messeges',
            name='Idd_Id',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
