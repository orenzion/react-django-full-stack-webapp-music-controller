# Generated by Django 3.2.8 on 2021-10-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='quest_can_pause',
            new_name='guest_can_pause',
        ),
    ]
