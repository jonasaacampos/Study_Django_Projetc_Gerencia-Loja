from django.shortcuts import render
from django.contrib import messages

from core.forms import ContatoForm



def index(request):
    return render(request, "index.html")


def contato(request):
    form = ContatoForm(request.POST or None)  # a vairável form será uma instância do nosso formulário

    # retorna um QueryDict com todos os dados do formulário
    # print(request.POST)

    if str(request.method) == "POST":
        if form.is_valid():
            form.send_mail()
            messages.success(request, "Mensagem enviada com sucesso.")
        else:
            messages.error(request, "erro ao enviar a mensagem")
            form = ContatoForm()

    context = {"form": form}
    return render(request, "contato.html", context)


def produto(request):
    return render(request, "produto.html")
