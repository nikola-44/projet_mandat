from django import forms
from .models import Contact


# Create your forms here.
class Contact(forms.Form):
    name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
