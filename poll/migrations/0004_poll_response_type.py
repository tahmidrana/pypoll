# Generated by Django 3.0.2 on 2020-02-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_poll_anonymous_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='response_type',
            field=models.SmallIntegerField(choices=[(1, 'Single Response'), (2, 'Multiple Response')], default=1),
        ),
    ]
