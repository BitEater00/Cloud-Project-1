# Generated by Django 3.2 on 2021-04-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='eventId',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='registration',
            name='studentId',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='clubId',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='studenId',
            field=models.CharField(max_length=200),
        ),
    ]
