# Generated by Django 5.2 on 2025-04-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_event_user_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="processed_text",
            field=models.TextField(blank=True, null=True),
        ),
    ]
