from django import forms

class Addition(forms.Form):
    Addition1 = forms.IntegerField(label='Number1')
    Addition2 = forms.IntegerField(label='Number2')

class Subtraction(forms.Form):
    Subtraction1 = forms.IntegerField(label='Number1')
    Subtraction2 = forms.IntegerField(label='Number2')

class Multiplication(forms.Form):
    Multiplication1 = forms.IntegerField(label='Number1')
    Multiplication2 = forms.IntegerField(label='Number2')

class Division(forms.Form):
    Division1 = forms.IntegerField(label='Number1')
    Division2 = forms.IntegerField(label='Number2')
