# Generated by Django 2.0 on 2019-06-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eamcetapp', '0004_auto_20190621_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_Name', models.CharField(max_length=20)),
                ('Rank', models.IntegerField()),
                ('College_Priority', models.CharField(max_length=20)),
            ],
        ),
    ]
