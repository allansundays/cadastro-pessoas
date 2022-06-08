from django import forms


class PessoaForm(forms.ModelForm):
    class Meta:
        models = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativo']