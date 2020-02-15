# Generated by Django 3.0.2 on 2020-02-15 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('student_roll_number', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
    ]
