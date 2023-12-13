# Generated by Django 4.2.6 on 2023-12-11 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0003_delete_employee_alter_company_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('about', models.TextField(max_length=300)),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('Human Resource', 'HR'), ('Project Leader', 'pl'), ('Software Developer', 'sd'), ('Fronted Developer', 'fd'), ('Backend Developer', 'bd')], max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestApi.company')),
            ],
        ),
    ]