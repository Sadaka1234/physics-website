from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2', )

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'placeholder':'Nombre de Usuario', 'size':'32'})
    self.fields['email'].widget.attrs.update({'placeholder': 'Dirección E-mail', 'size':'32'})
    self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña', 'size':'32'})
    self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Contraseña', 'size':'32'})

