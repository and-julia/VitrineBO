from django.shortcuts import render

# fazer o import das classes de form e model
from core.models import Cliente
from core.models import FormCliente

# definir o método que fará a request
def cadastroCliente(request):
    
    form = FormCliente(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        # definir o return se o formulário for válido
        return redirect('listagemClientes')

    # criar dicionário  de contexto com chave/valor dos returns ao render
    contexto = {'form': form, 'tipo': 'Cliente'}
    # renderizar a view com o caminho do arquivo
    return render(request, 'core/cadastro.html', contexto)