from django import forms
from .models import Customer, Courses, Meeting, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    massege = forms.CharField(max_length=200)  
    address = forms.CharField(max_length=200)  
    class Meta:
        model = Customer
        fields = ['userName', 'userMail', 'userPhone','massege','address']


class CoursesForm(forms.ModelForm):
    class Meta:
        model= Courses
        fields = '__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'