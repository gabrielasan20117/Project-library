from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(label='Name',required=True)
    birthday = forms.DateTimeField(label='Birthday',required=True)

class Editorial(forms.Form):
    name = forms.CharField(label='Name',required=True)