# Generated by Django 3.0.5 on 2022-03-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0004_auto_20220301_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_2',
            name='end_lect_three',
            field=models.TimeField(auto_created=True, null=True, verbose_name='lecture three end at'),
        ),
        migrations.AddField(
            model_name='day_2',
            name='lecture_three',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='lecture three'),
        ),
        migrations.AddField(
            model_name='day_2',
            name='start_lect_three',
            field=models.TimeField(null=True, verbose_name='lecture three start at'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='start_lect_tow',
            field=models.TimeField(null=True, verbose_name='lecture tow start at'),
        ),
    ]
