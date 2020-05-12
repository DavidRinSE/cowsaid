from django import forms
from cowsaid.models import Quote

class InputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)