# Generated by Django 2.2.28 on 2022-12-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_populate_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
