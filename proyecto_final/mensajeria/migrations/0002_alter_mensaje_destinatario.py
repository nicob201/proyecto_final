# Generated by Django 4.1.2 on 2022-11-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mensajeria", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mensaje",
            name="destinatario",
            field=models.CharField(max_length=100),
        ),
    ]
