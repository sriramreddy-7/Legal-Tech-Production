# Generated by Django 4.2.1 on 2024-04-24 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_casedocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='casedocument',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.appointment'),
        ),
        migrations.AddField(
            model_name='casedocument',
            name='is_accessible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='casedocument',
            name='shared_with_lsp',
            field=models.BooleanField(default=False),
        ),
    ]
