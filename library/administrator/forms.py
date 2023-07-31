from django import forms
class AuthorForm(forms.Form):
    name = forms.CharField(required=True)
    birthday = forms.DateTimeField(required=True)
    created_date = forms.DateTimeField(required=True)