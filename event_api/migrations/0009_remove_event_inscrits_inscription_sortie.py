# Generated by Django 4.2.5 on 2023-10-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0008_alter_event_options_alter_event_can_register_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='inscrits',
        ),
        migrations.AddField(
            model_name='inscription',
            name='sortie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_api.event'),
        ),
    ]
