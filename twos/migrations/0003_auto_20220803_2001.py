# Generated by Django 3.2.14 on 2022-08-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twos', '0002_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Status',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved')], default=0),
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback_made',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
