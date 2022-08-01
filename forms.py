import email
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .classe_viagem import tipos_de_classes

class PassagemForms(forms.Form):
    origem = forms.CharField(label='origem', max_length=100)
    destino = forms.CharField(label='destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='classe do voo', choices=tipos_de_classes)
    informacoes = forms.CharField(
        label='informacoes extras', 
        max_length=200,
        widget=forms.Textarea, 
        required=False
    )
    email = forms.EmailField(label='email', max_length=100)
    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('origem invalida')
        else:
            return origem

    def clean_destino(self):
        destino = self.cleaned_data.get('destino')
        if any(char.isdigit() for char in destino):
            raise forms.ValidationError('destino invalida')
        else:
            return destino

    

