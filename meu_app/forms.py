from django import forms
from .models import Equipamento
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'numero_patrimonio', 'tipo', 'em_uso']
        widgets = {
            'nome': forms.TextInput(attrs = {'class': 'form-control'}),
            'numero_patrimonio': forms.NumberInput(attrs = {'class': 'form-control'}),
            'tipo': forms.TextInput(attrs= {'class': 'form-control'}),
            'em_uso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }