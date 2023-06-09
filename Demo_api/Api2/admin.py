from django.contrib import admin
from Api2.models import Student
# Register your models here.

@admin.register(Student)
class StudebtAdmin(admin.ModelAdmin):
    list_display=['id','name','no','city']
