# Generated by Django 4.1.5 on 2023-01-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_participant_prefered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='prefered_date',
            field=models.JSONField(blank=True, null=True),
        ),
    ]