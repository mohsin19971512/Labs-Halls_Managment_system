# Generated by Django 3.0.5 on 2022-04-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0014_auto_20220303_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=50, verbose_name='Day'),
        ),
    ]
