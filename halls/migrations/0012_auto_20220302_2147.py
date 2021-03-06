# Generated by Django 3.0.5 on 2022-03-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0011_auto_20220301_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='end_lect_three',
            field=models.TimeField(auto_created=True, blank=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day',
            name='end_lect_tow',
            field=models.TimeField(auto_created=True, blank=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day',
            name='lect_one_given_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='given by'),
        ),
        migrations.AlterField(
            model_name='day',
            name='lect_three_given_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='given by'),
        ),
        migrations.AlterField(
            model_name='day',
            name='lect_tow_given_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='given by'),
        ),
        migrations.AlterField(
            model_name='day',
            name='start_lect_tow',
            field=models.TimeField(blank=True, null=True, verbose_name='Start at'),
        ),
    ]
