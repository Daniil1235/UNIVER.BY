# Generated by Django 5.1.6 on 2025-02-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0006_license_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='expired',
            field=models.BooleanField(default=False, verbose_name='Срок истёк'),
        ),
        migrations.AddField(
            model_name='license',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Ключ использован'),
        ),
    ]
