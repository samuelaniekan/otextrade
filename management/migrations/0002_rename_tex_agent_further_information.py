# Generated by Django 4.0.5 on 2022-06-28 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='tex',
            new_name='further_information',
        ),
    ]
