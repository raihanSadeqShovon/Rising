import email
from django import forms

class TeachersRegistration(forms.Form):
    first_name = forms.CharField(label='Enter your first name', label_suffix='')
    last_name = forms.CharField(initial='Sadeq')
    email = forms.EmailField(initial='raihan@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)
    