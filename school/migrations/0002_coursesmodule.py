# Generated by Django 4.1 on 2024-01-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoursesModule",
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
                ("className", models.CharField(max_length=20)),
                ("poster", models.ImageField(upload_to="courses")),
                ("category", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("instructor", models.CharField(max_length=50)),
                ("heading", models.CharField(max_length=35)),
            ],
        ),
    ]