# Generated by Django 4.1.5 on 2023-01-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_meeting_participants_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='prefered_date',
            field=models.JSONField(blank=True),
        ),
    ]
