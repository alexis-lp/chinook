from django import forms


class SearchForm(forms.Form):
    album = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'size': 40}))
