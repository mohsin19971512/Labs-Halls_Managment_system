# Generated by Django 3.0.5 on 2022-03-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0013_auto_20220302_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='end_lect_one',
            field=models.TimeField(blank=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day',
            name='end_lect_three',
            field=models.TimeField(blank=True, null=True, verbose_name='End at'),
        ),
        migrations.AlterField(
            model_name='day',
            name='end_lect_tow',
            field=models.TimeField(blank=True, null=True, verbose_name='End at'),
        ),
    ]
