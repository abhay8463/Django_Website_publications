# Generated by Django 3.0.5 on 2020-06-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRCpubs', '0007_auto_20200609_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrcpubs',
            name='publishedAt',
            field=models.DateField(),
        ),
    ]
