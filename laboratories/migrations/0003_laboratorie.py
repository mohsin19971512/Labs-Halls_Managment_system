# Generated by Django 3.0.5 on 2022-03-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('halls', '0009_auto_20220301_2146'),
        ('laboratories', '0002_delete_laboratorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('numbers_of_computer', models.IntegerField(null=True, verbose_name='Numbers of Computer')),
                ('working_computers', models.IntegerField(null=True, verbose_name='Working Computers')),
                ('computers_not_working', models.IntegerField(null=True, verbose_name='Computers not working')),
                ('days', models.ManyToManyField(to='halls.Day')),
            ],
        ),
    ]
