from django import forms

class MateriaForm(forms.Form):
  materias = forms.CharField(label='topico', max_length=100)
