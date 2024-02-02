# Generated by Django 4.2 on 2024-02-01 03:06

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(limit_value=3)])),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
