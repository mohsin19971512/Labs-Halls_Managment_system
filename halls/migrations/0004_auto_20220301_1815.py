# Generated by Django 3.0.5 on 2022-03-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0003_auto_20220301_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_2',
            name='lecture_tow',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='lecture tow'),
        ),
    ]
