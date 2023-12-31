# Generated by Django 5.0 on 2023-12-19 07:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=12, null=True)),
                ('customer_number', models.CharField(blank=True, max_length=20, null=True)),
                ('meter_serial_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
