# Generated by Django 3.0.5 on 2022-05-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0017_auto_20220407_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=50, verbose_name='Day'),
        ),
    ]