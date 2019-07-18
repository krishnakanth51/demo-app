from .models import StudentData ,CollegeData,Register
from django import forms
from django.forms import ModelForm
class Student_Form(forms.ModelForm):
    class Meta:
            model=StudentData
            fields='__all__'
            
            

class LoginForm(forms.Form):
    Eamcet_Rank= forms.IntegerField(
        label='Eamcet_Rank',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Rank'
            }

        )

    )

class CollegeForm(forms.ModelForm):
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
    #Col_Name= forms.MultipleChoiceField(choices =colleges ,widget=forms.CheckboxSelectMultiple(), required=False)
    #Universitys= forms.MultipleChoiceField(choices =Universitys ,widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model=CollegeData
        fields=['University','College_Name','College_Code','College_Address','Rank_limit']
            
              #exclude=['Eamcet_Rank','Email','Inter_Percent']

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
class RegisterForm(forms.ModelForm):
    College_Priority= forms.MultipleChoiceField(choices = colleges,widget=forms.CheckboxSelectMultiple(), 
        required=False)
    class Meta:
            model=Register
            fields="__all__"

# class EmailSendForm(forms.ModelForm):
#     class Meta:
#         model=EmailSendModel
#         fields='__all__'


