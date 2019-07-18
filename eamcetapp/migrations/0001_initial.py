# Generated by Django 2.0 on 2019-06-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_Name', models.CharField(max_length=30)),
                ('Pre_Col_Name', models.CharField(max_length=30)),
                ('Inter_Percent', models.FloatField()),
                ('Eamcet_Rank', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
