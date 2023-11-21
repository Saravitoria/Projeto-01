from django import forms
from .models import Filme, Comentarios


class Filmeform(forms.ModelForm):
    class Meta:
        model=Filme
        fields='__all__' 

class Coment(forms.ModelForm):
    class Meta:
        model=Comentarios
        fields='__all__'        