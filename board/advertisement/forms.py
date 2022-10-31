from django import forms
from .models import CalcHistory


class HistoryForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        self.instance.result = self.initial['result']
        return super(HistoryForm, self).save(*args, **kwargs)
    class Meta:
        model = CalcHistory
        fields = ['val1', 'val2', 'operator']