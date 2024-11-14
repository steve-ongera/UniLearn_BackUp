from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control placeholder-1', 'id': 'exampleInputTitle1'}),
            'email': forms.EmailInput(attrs={'class': 'form-control placeholder-1', 'id': 'exampleInputTitle2'}),
            'message': forms.Textarea(attrs={'class': 'form-control placeholder-1', 'id': 'exampleFormControlTextarea1', 'rows': 6}),
        }
