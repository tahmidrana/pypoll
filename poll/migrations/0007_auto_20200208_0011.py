# Generated by Django 3.0.2 on 2020-02-07 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_submissionoption'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pollsubmission',
            unique_together=set(),
        ),
    ]
