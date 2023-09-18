# Generated by Django 4.2.4 on 2023-09-17 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "chat_noti",
            "0002_chat_alter_message_options_remove_message_message_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="receiver",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="message_receiver",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="chat",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="message",
            name="chat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="chat_noti.chat"
            ),
        ),
    ]
