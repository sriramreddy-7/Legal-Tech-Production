# Generated by Django 4.2.1 on 2024-04-23 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_alter_profile_account_type_alter_profile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_start', models.TimeField(blank=True, null=True)),
                ('monday_end', models.TimeField(blank=True, null=True)),
                ('tuesday_start', models.TimeField(blank=True, null=True)),
                ('tuesday_end', models.TimeField(blank=True, null=True)),
                ('wednesday_start', models.TimeField(blank=True, null=True)),
                ('wednesday_end', models.TimeField(blank=True, null=True)),
                ('thursday_start', models.TimeField(blank=True, null=True)),
                ('thursday_end', models.TimeField(blank=True, null=True)),
                ('friday_start', models.TimeField(blank=True, null=True)),
                ('friday_end', models.TimeField(blank=True, null=True)),
                ('saturday_start', models.TimeField(blank=True, null=True)),
                ('saturday_end', models.TimeField(blank=True, null=True)),
                ('sunday_start', models.TimeField(blank=True, null=True)),
                ('sunday_end', models.TimeField(blank=True, null=True)),
                ('service_provider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=100)),
                ('case_type', models.CharField(max_length=100)),
                ('case_info', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_appointments', to=settings.AUTH_USER_MODEL)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
