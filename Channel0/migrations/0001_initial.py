# Generated by Django 4.1.2 on 2022-10-21 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='None', max_length=20, null=True)),
                ('profile_pic', models.ImageField(default='profile.png', null=True, upload_to='')),
                ('police_number', models.IntegerField(null=True)),
                ('rank', models.CharField(max_length=20)),
                ('telephone', models.IntegerField(null=True)),
                ('faculty', models.CharField(blank=True, choices=[(' Modern Languages', 'Modern Languages'), ('Ict', 'Ict'), ('PPS', 'PPS'), ('Law', 'Law')], default='None', max_length=20, null=True)),
                ('level', models.CharField(blank=True, choices=[(' Level I', 'Level I'), ('Level II', 'Level II'), ('Level III', 'Level III'), ('IV', 'Level IV')], default='None', max_length=20, null=True)),
                ('registration_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
