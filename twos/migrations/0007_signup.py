# Generated by Django 3.2.14 on 2022-08-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twos', '0006_auto_20220804_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
