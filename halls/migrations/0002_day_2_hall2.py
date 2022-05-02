# Generated by Django 3.0.5 on 2022-03-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_lect_tow', models.TimeField(auto_created=True, null=True, verbose_name='end at')),
                ('end_lect_one', models.TimeField(auto_created=True, null=True, verbose_name='end at')),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=50, verbose_name='Day')),
                ('lecture_one', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=50, null=True, verbose_name='lecture one')),
                ('start_lect_one', models.TimeField(null=True, verbose_name='start at')),
                ('lecture_tow', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=50, null=True, verbose_name='lecture tow')),
                ('start_lect_tow', models.TimeField(null=True, verbose_name='start at')),
            ],
        ),
        migrations.CreateModel(
            name='Hall2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('seats', models.IntegerField(null=True, verbose_name='Seats')),
                ('days', models.ManyToManyField(to='halls.Day_2')),
            ],
        ),
    ]
