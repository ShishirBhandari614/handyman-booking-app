# Generated by Django 5.1.3 on 2025-01-19 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kycverification', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='service_provider',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kyc', to=settings.AUTH_USER_MODEL),
        ),
    ]
