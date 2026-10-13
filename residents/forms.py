from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DocumentRequest, Complaint

class ResidentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']

class DocumentRequestForm(forms.ModelForm):
    class Meta:
        model = DocumentRequest
        fields = ['document_type', 'purpose']
        widgets = {
            'purpose': forms.Textarea(attrs={'rows': 4, 'placeholder': 'State your reason for requesting this document...'}),
        }

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject', 'details']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Short title of your complaint'}),
            'details': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your complaint in detail...'}),
        }