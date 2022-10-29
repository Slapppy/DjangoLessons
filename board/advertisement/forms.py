from django import forms
from .models import CalcHistory


class HistoryForm(forms.ModelForm):
    class Meta:
        model = CalcHistory
        fields = ['val1', 'val2', 'operator']
