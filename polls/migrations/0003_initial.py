# Generated by Django 4.1.3 on 2022-11-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0002_delete_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('countrycode', models.CharField(max_length=3)),
            ],
        ),
    ]
