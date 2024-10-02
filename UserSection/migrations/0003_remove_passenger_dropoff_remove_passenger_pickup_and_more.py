# Generated by Django 4.1.2 on 2023-05-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSection', '0002_remove_customuser_name_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='dropoff',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='pickup',
        ),
        migrations.AddField(
            model_name='passenger',
            name='location',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
