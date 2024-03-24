# Generated by Django 4.1 on 2024-01-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0006_alter_schedulemodule_isdone"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamDeatilsModule",
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
                ("selfie", models.ImageField(upload_to="team")),
                ("category", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=30)),
                ("facebook", models.TextField()),
                ("twitter", models.TextField()),
                ("linkedin", models.TextField()),
            ],
        ),
    ]