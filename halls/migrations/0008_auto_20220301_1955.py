# Generated by Django 3.0.5 on 2022-03-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0007_hall2_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall2',
            name='supervisor',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='supervisor'),
        ),
    ]
