from django.shortcuts import render,redirect
from .models import StudentData,CollegeData,Register
from .forms import Student_Form,CollegeForm,LoginForm,CollegeForm,RegisterForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError,EmailMessage
import random

global Rank
def HomeView(request):
    collegelist=CollegeData.objects.all()
    Rform=RegisterForm()
    if request.method=="POST":
        Rform=RegisterForm(request.POST)
        if Rform.is_valid():
            Eamcet_Rank=request.POST.get('Eamcet_Rank','')
            a=Eamcet_Rank
            Student_Name=request.POST.get('Student_Name','')
            Email=request.POST.get('Email','')
            data=Register(
                Student_Name=Student_Name,
                Eamcet_Rank=Eamcet_Rank,
                Email=Email
            )
            data.save()
            return redirect(Email_Sending,Email)
    return render(request,'eamcetapp/home.html',{'collegelist':collegelist,'Rform':Rform})


def StudentDataView(request):
    form=Student_Form()
    if request.method=="POST":
        form=Student_Form(request.POST)
        if form.is_valid():
            data=StudentData(
                Student_Name=request.POST.get('Student_Name',''),
                Previous_College_Name=request.POST.get('Previous_College_Name',''),
                Inter_Percent=request.POST.get('Inter_Percent',''),
                Eamcet_Rank=request.POST.get('Eamcet_Rank',''),
                Email=request.POST.get('Email',''),
            )
            a=form.cleaned_data['Eamcet_Rank']
            #b=form.cleaned_data['']
            form.cleaned_data["Eamcet_Rank"]=int(a)
            data.save()
            form=Student_Form()
            return render(request,'eamcetapp/studentdata.html',{'form':form})
    return render(request,'eamcetapp/studentdata.html',{'form':form})

def HomeView(request):
    collegelist=CollegeData.objects.all()
    Rform=RegisterForm()
    if request.method=="POST":
        Rform=RegisterForm(request.POST)
        if Rform.is_valid():
            Eamcet_Rank=request.POST.get('Eamcet_Rank','')
            a=Eamcet_Rank
            Student_Name=request.POST.get('Student_Name','')
            Email=request.POST.get('Email','')
            data=Register(
                Student_Name=Student_Name,
                Eamcet_Rank=Eamcet_Rank,
                Email=Email
            )
            data.save()
            return redirect(Email_Sending,Email)
    return render(request,'eamcetapp/home.html',{'collegelist':collegelist,'Rform':Rform})
def Loginview(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            Rank1=request.POST.get('Eamcet_Rank','')
            try:
                Student=StudentData.objects.filter(Eamcet_Rank=Rank1)
                if Student:
                    #User_Names=.objects.filter(Eamcet_Rank=Rank)
                    return redirect('/homepage')#render(request,'eamcetapp/home.html',{'Student':Student})
                else:
                    return HttpResponse("InValid Rank")
            except StudentData.DoesNotExist:
                msg="UserName and Password Does Not Match"
                return render(request,'eamcetapp/login.html',{"msg":msg})
    else:
        logform=LoginForm()
        return render(request,'eamcetapp/login.html', {'form':logform})


def Email_Sending(request,Email):
    To=Email
    From='sekharpajjuri'
    Sub='regardng Eamcet concelling'
    Message='you selectd'
    try:
        mail = EmailMessage(Sub,From,Message,[To,])
        #mail.attach(File_Attach.name, File_Attach.read(),File_Attach.content_type)
        mail.send()
        
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    #return HttpResponse('Email sent success')
    Eamcet_Rank=StudentData.objects.filter(Email=Email)
    return redirect(Assign_List_View,Eamcet_Rank)

def Assign_List_View(request,Eamcet_Rank):
    Rank=Eamcet_Rank
    col_data=CollegeData.objects.filter(Rank_limit__lt=Rank)
    return render(request,'eamcetapp/assigndlist.html',{'col_data':col_data})


def HomeView(request):
    collegelist=CollegeData.objects.all()
    Rform=RegisterForm()
    if request.method=="POST":
        Rform=RegisterForm(request.POST)
        if Rform.is_valid():
            Eamcet_Rank=request.POST.get('Eamcet_Rank','')
            a=Eamcet_Rank
            Student_Name=request.POST.get('Student_Name','')
            Email=request.POST.get('Email','')
            data=Register(
                Student_Name=Student_Name,
                Eamcet_Rank=Eamcet_Rank,
                Email=Email
            )
            data.save()
            return redirect(Email_Sending,Email)
    return render(request,'eamcetapp/home.html',{'collegelist':collegelist,'Rform':Rform})

def RegisterView(request):
    Rform=RegisterForm()
    if request.method=="POST":
        Rform=RegisterForm(request.POST)
        if Rform.is_valid():
            Eamcet_Rank=request.POST.get('Eamcet_Rank','')
            a=Eamcet_Rank
            Stu_Name=request.POST.get('Student_Name','')
            #return redirect(AssignView(request,Eamcet_Rank,Stu_Name))
            return HttpResponse('Success')
    else:
        return render(request,'eamcetapp/register.html',{'Rform':Rform})

    

# def ConcelingView(req)


def CollegeView(request):
    form=CollegeForm()
    if request.method=="POST":
        form=CollegeForm(request.POST)
        if form.is_valid():
            Rank_limit1= request.POST.get('Rank_limit','')
            
            data=CollegeData(
                College_Name=request.POST.get('College_Name',''),
                College_Code=request.POST.get('College_Code',''),
                College_Address=request.POST.get('College_Address',''),
                University=request.POST.get('University',''),
                Rank_limit=str(Rank_limit1)
            )
           
            a=form.cleaned_data['Rank_limit']
            form.cleaned_data["Rank_limit"]=int(a)
            form.save()
            form=CollegeForm()
            return render(request,'eamcetapp/collegedata.html',{'form':form})
    return render(request,'eamcetapp/collegedata.html',{'form':form})


