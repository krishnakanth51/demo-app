# Generated by Django 2.0 on 2019-06-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eamcetapp', '0008_auto_20190622_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Email',
            field=models.EmailField(default='@gmail.com', max_length=254),
        ),
    ]
