from django import forms


class SearchForm(forms.Form):
    recherche = forms.CharField()
