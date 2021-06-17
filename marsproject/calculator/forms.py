from django import forms 

class CalculateMars(forms.Form):
    age = forms.IntegerField(label="Age")
    weight = forms.IntegerField(label="Weight")