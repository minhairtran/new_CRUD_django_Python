from django import forms

from Student.models import Student

class StudentModelForm(forms.ModelForm):
    identity_number = forms.IntegerField(max_value=100000000, min_value=20000000)
    name = forms.CharField(label='Name: ', widget=forms.TextInput(
        attrs={"placeholder": "Type in your name"}
    ))
    age = forms.IntegerField(max_value=100)
    hometown = forms.CharField(max_length=100)
    CPA = forms.DecimalField(decimal_places=2, label='CPA')

    class Meta:
        model = Student
        fields = [
            'identity_number',
            'name',
            'age',
            'hometown',
            'CPA',
        ]

class StudentCreateForm(StudentModelForm):

    class Meta:
        model = Student
        fields = [
            'identity_number',
            'name',
            'age',
            'hometown',
            'CPA',
        ]
    
    


    
