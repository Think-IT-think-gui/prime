# Generated by Django 3.2.10 on 2022-10-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0020_user_messeges'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.CharField(max_length=100)),
                ('Chat_Id', models.CharField(max_length=100)),
            ],
        ),
    ]
