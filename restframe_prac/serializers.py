from rest_framework import serializers
from restframe_prac.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields = ['name','age','father_name']

    def validate(self, attrs):
        print(attrs)
        age = attrs.get('age')
        if age < 18:
            print(age)
            raise serializers.ValidationError({"age":"Age must be greater then 18 years!!!"})
        return attrs
    
    def validate_name(self,value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError({"error":"Digit is not Allowed!!!"})
        return value