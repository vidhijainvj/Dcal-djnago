# Generated by Django 4.1.2 on 2022-11-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_alter_event_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="time",
            new_name="start_time",
        ),
        migrations.AddField(
            model_name="event",
            name="end_time",
            field=models.TimeField(default="12:00:00"),
            preserve_default=False,
        ),
    ]
