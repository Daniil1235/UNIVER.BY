# Generated by Django 5.1.5 on 2025-01-30 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_license_key_user_licensed'),
        ('premium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='license_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='premium.license'),
        ),
    ]
