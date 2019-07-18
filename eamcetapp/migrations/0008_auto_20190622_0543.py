# Generated by Django 2.0 on 2019-06-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eamcetapp', '0007_register_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Rank',
            new_name='Eamcet_Rank',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Stu_Name',
            new_name='Student_Name',
        ),
        migrations.AlterField(
            model_name='collegedata',
            name='College_Name',
            field=models.CharField(choices=[('S.S & N ', 'S.S & N'), ('Srinivasa Initute of Eng and Tech', 'Srinivasa Initute of Eng and Tech'), ('Sri Mittapalli College of Eng and Tech', 'Sri Mittapalli College of Eng and Tech'), ('Andhra cristian college', 'Andhra cristian college'), ('VVIT', 'VVIT'), ('Nalandha college of Eng and Tech', 'Nalandha college of Eng and Tech'), ('Sri Chaitanya college of Eng and Tech', 'Sri Chaitanya college of Eng and Tech'), ('A.M.Reddy College', 'A.M.Reddy College'), ('Amara College of Eng and Tech', 'Amara College of Eng and Tech'), ('M.A.M College of Eng and Tech', 'M.A.M College of Eng and Tech'), ('National Initute of Technology', 'National Initute of Technology'), ('Gayatri Viddya Prasad Of College', 'Gayatri Viddya Prasad Of College'), ('Sidhardha Inititute of Eng and Tech', 'Sidhardha Inititute of Eng and Tech'), ('Sri Vidhyaniketan Eng and Tech', 'Sri Vidhyaniketan Eng and Tech')], max_length=100),
        ),
        migrations.AlterField(
            model_name='collegedata',
            name='University',
            field=models.CharField(choices=[('Acharya Nagarjuna University', 'Acharya Nagarjuna University'), ('Acharya N.G. Ranga Agricultural University', 'Acharya N.G. Ranga Agricultural University'), ('Andhra University ', 'Andhra University'), ('Damodaram Sanjivayya National Law University', 'Damodaram Sanjivayya National Law University'), ('Dr. Y.S.R. Horticultural University', 'Dr. Y.S.R. Horticultural University'), ('Dravidian University', 'Dravidian University'), ('Gurazada Apparao University', 'Gurazada Apparao University'), ('Dr. NTR University of Health Sciences', 'Dr. NTR University of Health Sciences'), ('Jawaharlal Nehru Technological University', 'Jawaharlal Nehru Technological University'), ('Krishna University', 'Krishna University')], max_length=100),
        ),
    ]