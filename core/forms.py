# importar o nome das classes do models
from core.models import Cliente
from django.forms import ModelForm

# criar classe de formulário chamando o método ModelForm
class FormCliente(ModelForm):
    class Meta:
        # nome da classe a ser chamada
        model = Cliente
        # atributos a serem chamados
        fields = '__all__'