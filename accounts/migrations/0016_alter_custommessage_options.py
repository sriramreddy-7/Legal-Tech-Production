# Generated by Django 4.2.1 on 2024-04-25 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_custommessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custommessage',
            options={'ordering': ['timestamp']},
        ),
    ]
