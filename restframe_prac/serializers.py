from rest_framework import serializers
from restframe_prac.models import Student,Category,Book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        # fields = ['name','age','father_name']
        fields = "__all__"

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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ['category_name']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer() #use when just want custom data fields from the category  like:- category_name only
    class Meta:
        model = Book
        fields = "__all__"
        # depth = 1       #use when just want to all the data fields from category like :- id,name etc "__all__" all fields