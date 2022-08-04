# Generated by Django 3.2.14 on 2022-08-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twos', '0004_menu_menu_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved')], default=0),
        ),
    ]
