# Generated by Django 5.1.5 on 2025-01-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0002_alter_license_options_alter_plan_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='key',
            field=models.CharField(blank=True, default='6t4hj-68722-x4qn0-16td6-f91w5', max_length=100, verbose_name='Ключ'),
        ),
    ]
