# Generated by Django 3.1.4 on 2021-01-04 12:01

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ("timesup", "0002_auto_20210104_1133"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="state",
            field=django_fsm.FSMField(default="created", max_length=50),
        ),
    ]
