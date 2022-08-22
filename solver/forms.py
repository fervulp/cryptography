from django import forms

class ShamirForm(forms.Form):
    p =  forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='p')
    x1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='x1')
    y1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='y1')
    X1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='X1')

class DiffieHellmanForm(forms.Form):
    p =  forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='p')
    g = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='g')
    x = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='x')
    y = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='y')

class ElGamalEForm(forms.Form):
    p =  forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='p')
    g = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='g')
    y = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='y')
    M = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='M')
    k = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='k')

class ElGamalDForm(forms.Form):
    p =  forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='p')
    g = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='g')
    x = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='x')
    r = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='r')
    s = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}), label='s')