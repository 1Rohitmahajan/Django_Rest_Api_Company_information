# Generated by Django 4.2.6 on 2023-12-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
