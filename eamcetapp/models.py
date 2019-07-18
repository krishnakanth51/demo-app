from django.db import models

class StudentData(models.Model):
    Student_Name=models.CharField(max_length=30)
    Previous_College_Name=models.CharField(max_length=30)
    Inter_Percent=models.FloatField(default=None)
    Eamcet_Rank=models.IntegerField(unique=True)
    Email=models.EmailField(default="@gmail.com")

    def __str__(self):
        return self.Student_Name


class CollegeData(models.Model):
    colleges=[
        ('S.S & N ','S.S & N'),('Srinivasa Initute of Eng and Tech','Srinivasa Initute of Eng and Tech'),
        ('Sri Mittapalli College of Eng and Tech','Sri Mittapalli College of Eng and Tech'),
        ('Andhra cristian college','Andhra cristian college'),('VVIT','VVIT'),
        ('Nalandha college of Eng and Tech','Nalandha college of Eng and Tech'),
        ('Sri Chaitanya college of Eng and Tech','Sri Chaitanya college of Eng and Tech'),
        ('A.M.Reddy College','A.M.Reddy College'),('Amara College of Eng and Tech','Amara College of Eng and Tech'),
        ('M.A.M College of Eng and Tech','M.A.M College of Eng and Tech'),('National Initute of Technology','National Initute of Technology'),
        ('Gayatri Viddya Prasad Of College','Gayatri Viddya Prasad Of College'),('Sidhardha Inititute of Eng and Tech','Sidhardha Inititute of Eng and Tech'),
        ('Sri Vidhyaniketan Eng and Tech','Sri Vidhyaniketan Eng and Tech')
        ]
    Universitys=[
        ('Acharya Nagarjuna University','Acharya Nagarjuna University'),
        ('Acharya N.G. Ranga Agricultural University','Acharya N.G. Ranga Agricultural University'),
        ('Andhra University ','Andhra University'),('Damodaram Sanjivayya National Law University','Damodaram Sanjivayya National Law University'),
        ('Dr. Y.S.R. Horticultural University','Dr. Y.S.R. Horticultural University'),('Dravidian University','Dravidian University'),
        ('Gurazada Apparao University','Gurazada Apparao University'),('Dr. NTR University of Health Sciences','Dr. NTR University of Health Sciences'),
        ('Jawaharlal Nehru Technological University','Jawaharlal Nehru Technological University'),('Krishna University','Krishna University')
    ]
    University=models.CharField(max_length=100,choices=Universitys)
    College_Name=models.CharField(max_length=100,choices=colleges)
    College_Code=models.CharField(max_length=20)
    College_Address=models.CharField(max_length=20)
    Rank_limit=models.CharField(max_length=10)

    def __str__(self):
        return self.College_Name

class Register(models.Model):
    Student_Name=models.CharField(max_length=20)
    Eamcet_Rank=models.CharField(max_length=10)
    College_Priority=models.CharField(max_length=500)
    Email=models.EmailField(default="@gmail.com")

# class EmailSendModel(models.Model):
#     From=models.EmailField(default='@gmail.com')
#     To=models.EmailField(default='@gmail.com')
#     Subject = models.CharField(max_length=100)
#     Attach= models.FileField(upload_to='senddoc/')
#     Message = models.TextField(max_length=250)



    