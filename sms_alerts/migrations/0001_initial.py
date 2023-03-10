# Generated by Django 4.1.7 on 2023-02-24 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SmsAlert",
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
                ("phone_number", models.CharField(blank=True, max_length=20)),
                ("location", models.CharField(max_length=100)),
                (
                    "air_quality_threshold",
                    models.CharField(
                        choices=[
                            ("Good", "Good"),
                            ("Moderate", "Moderate"),
                            (
                                "Unhealthy for Sensitive Groups",
                                "Unhealthy for Sensitive Groups",
                            ),
                            ("Unhealthy", "Unhealthy"),
                            ("Very Unhealthy", "Very Unhealthy"),
                            ("Hazardous", "Hazardous"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "previous_air_quality_threshold_alert",
                    models.CharField(blank=True, max_length=100),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alerts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
