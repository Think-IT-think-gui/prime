# Generated by Django 3.2.10 on 2022-10-24 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0025_message_api'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_messeges',
            name='Time',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user_messeges',
            name='date',
            field=models.CharField(max_length=500),
        ),
    ]