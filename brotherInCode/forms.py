from django import forms
from django.forms import ModelForm
from .models import Tutoria

class Matricula(ModelForm):
    class Meta:
        model = Tutoria
        fields = ('id_tutoria', 'id_tutor', 'id_aluno', 'id_sub_area_conhecimento','id_horario_tutor', 'data', 'link', 'status')
        widgets = {
            'data': forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'link': forms.TextInput(attrs={'placeholder': 'https://site.com'}),
        }