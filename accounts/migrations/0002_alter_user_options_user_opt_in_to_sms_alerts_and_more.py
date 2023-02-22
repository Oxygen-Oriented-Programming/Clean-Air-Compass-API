# Generated by Django 4.1.7 on 2023-02-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["last_name", "first_name"],
                "verbose_name_plural": "users",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="opt_in_to_sms_alerts",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
