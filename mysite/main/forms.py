from django import forms
#a Class object that creates new to do lists from the form entries and assigns them to properties
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)