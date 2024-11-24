from django.forms import forms
class form(forms.Form):
    name = forms.CharField(max_length=100)
    