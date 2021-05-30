from django import forms
from django.forms import fields
from app.models import *

class NameForm(forms.Form):
    name=forms.CharField(max_length=200)


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
