# Generated by Django 3.0.6 on 2020-06-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0002_auto_20200524_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': [('update_rating', 'Can update rating')]},
        ),
    ]
