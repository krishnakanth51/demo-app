# Generated by Django 2.0 on 2019-06-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eamcetapp', '0009_auto_20190622_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='College_Priority',
            field=models.CharField(max_length=500),
        ),
    ]
