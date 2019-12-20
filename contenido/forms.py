from django import forms

class TopicoForm(forms.Form):
  topico = forms.CharField(max_length=50)
