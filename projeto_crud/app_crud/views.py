from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # Criando um novo usuário no banco
    novo_usuario = Usuario()

    # Usando as informações do form
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')

    # Salvando os dados
    novo_usuario.save()

    # Exibir os usuários, o django espera um dicionário
    usuarios = {
        'usuarios': Usuario.objects.all()

    }

    return render(request, 'usuarios/usuarios.html', usuarios)