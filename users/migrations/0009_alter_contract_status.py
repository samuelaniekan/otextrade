# Generated by Django 4.0.5 on 2022-07-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_contract_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=100, null=True),
        ),
    ]
