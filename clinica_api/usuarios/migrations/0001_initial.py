# Generated by Django 4.1.7 on 2023-03-23 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tutor",
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
                ("nome", models.CharField(max_length=100)),
                ("cpf", models.CharField(max_length=11)),
                (
                    "data_nascimento",
                    models.DateField(verbose_name="Data de nascimento"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Animal",
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
                ("nome", models.CharField(max_length=50)),
                ("raça", models.CharField(max_length=50)),
                ("cor", models.CharField(max_length=50)),
                (
                    "data_nascimento",
                    models.DateField(verbose_name="Data de nascimento"),
                ),
                (
                    "tutor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="usuarios.tutor"
                    ),
                ),
            ],
        ),
    ]