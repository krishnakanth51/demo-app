# Generated by Django 2.0 on 2019-06-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eamcetapp', '0006_auto_20190621_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
