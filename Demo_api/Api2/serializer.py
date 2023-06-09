from optparse import Values
from .models import Student
from rest_framework import  serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','no','city']

    # def validate_no(self,value):
    #     if value.isalpha():
    #         raise serializers.ValidationError('please enter onlu number')
    #     return value    