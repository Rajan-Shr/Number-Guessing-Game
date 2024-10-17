from django import forms
from .models import Number
class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ('number',)
    
    # number = forms.IntegerField(widget=forms.IntegerField())
    number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder':"Enter any number",
        'class':"w-500 py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-center text-lg"
    }))