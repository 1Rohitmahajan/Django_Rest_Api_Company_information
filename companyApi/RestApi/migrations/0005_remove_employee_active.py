# Generated by Django 4.2.6 on 2023-12-11 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0004_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='active',
        ),
    ]
