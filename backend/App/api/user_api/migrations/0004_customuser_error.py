# Generated by Django 4.2 on 2023-04-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_customuser_address_customuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='error',
            field=models.CharField(default='None', max_length=100),
        ),
    ]