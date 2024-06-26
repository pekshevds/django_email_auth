# Generated by Django 4.1 on 2024-06-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$YRiKxVT0IiDLkLReHK4G80$juyF15JRRsBTZiuKMIhIWkSpN/DuU9uvsA3zz37Wx7A=', max_length=128, verbose_name='password'),
        ),
    ]
