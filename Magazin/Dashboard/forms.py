# forms.py
from django import forms
from .models import Reader, Writer

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['phone', 'is_darkmode']  # Add other fields as necessary
        # Optionally include widgets and labels customization

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['phone', 'is_darkmode']  # Add other fields as necessary
        # Optionally include widgets and labels customization
