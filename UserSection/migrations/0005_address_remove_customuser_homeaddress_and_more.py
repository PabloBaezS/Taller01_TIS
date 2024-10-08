# Generated by Django 4.2.16 on 2024-10-02 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UserSection", "0004_alter_driver_customuser_ptr_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="homeAddress",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="capacity",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="color",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="driverId",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="licensePlate",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="model",
        ),
        migrations.AddField(
            model_name="vehicle",
            name="license_plate",
            field=models.CharField(default="UNKNOWN", max_length=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="UserSection.address",
            ),
        ),
    ]
