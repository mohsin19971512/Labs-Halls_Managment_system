# Generated by Django 3.0.5 on 2022-03-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0005_auto_20220301_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_2',
            name='lect_one_given_by',
            field=models.CharField(max_length=50, null=True, verbose_name='given by'),
        ),
        migrations.AddField(
            model_name='day_2',
            name='lect_three_given_by',
            field=models.CharField(max_length=50, null=True, verbose_name='given by'),
        ),
        migrations.AddField(
            model_name='day_2',
            name='lect_tow_given_by',
            field=models.CharField(max_length=50, null=True, verbose_name='given by'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='end_lect_one',
            field=models.TimeField(auto_created=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='end_lect_three',
            field=models.TimeField(auto_created=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='end_lect_tow',
            field=models.TimeField(auto_created=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='start_lect_one',
            field=models.TimeField(null=True, verbose_name='Start at'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='start_lect_three',
            field=models.TimeField(null=True, verbose_name='Start at'),
        ),
        migrations.AlterField(
            model_name='day_2',
            name='start_lect_tow',
            field=models.TimeField(null=True, verbose_name='Start at'),
        ),
    ]