# Generated by Django 4.1 on 2024-06-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$dQK3olTQx33XBFYe09bZb8$J+xic3wdt+31w62N6y9HjxHUg1uHrKE6mWeq2TmObu0=', max_length=128, verbose_name='password'),
        ),
    ]
