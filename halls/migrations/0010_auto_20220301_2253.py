# Generated by Django 3.0.5 on 2022-03-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0009_auto_20220301_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='lecture_one',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='lecture one'),
        ),
    ]