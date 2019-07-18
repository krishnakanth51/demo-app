from django.contrib import admin

from .models import StudentData,CollegeData

class StudentAdmin(admin.ModelAdmin):
    list_display=['Student_Name','Previous_College_Name','Inter_Percent','Eamcet_Rank','Email']

admin.site.register(StudentData,StudentAdmin)

class CollegeAdmin(admin.ModelAdmin):
    ist_display=['College_Name','College_Code','College_Address','Rank_limit']

admin.site.register(CollegeData,CollegeAdmin)