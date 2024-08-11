# calculator/forms.py
from django import forms


class CalculationForm(forms.Form):
    expression = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter expression, e.g. 2 + 2 * 3'
    }))
