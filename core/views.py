from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from core.forms import ContatoForm, ProdutoModelForm
from .models import Produto


def dev_show_data_product_pre_save(produto, form):
    produto = form.save(commit=False)
    print(
        f"""
     nome: {produto.nome}\n
     preço: {produto.preco}\n
     estoque: {produto.estoque}\n
     imagem: {produto.imagem}
     """
    )


def index(request):
    context = {"produtos": Produto.objects.all()}
    return render(request, "index.html", context)


def contato(request):
    form = ContatoForm(
        request.POST or None
    )  # a vairável form será uma instância do nosso formulário

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

    if str(request.user) != "AnonymousUser":
        if str(request.method) == "POST":
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Produto salvo com sucesso.")
                form = ProdutoModelForm()
            else:
                messages.error(
                    request, "Erro ao salvar... tente novamente após alguns minutos"
                )

        else:
            form = ProdutoModelForm()
        context = {"form": form}
        return render(request, "produto.html", context)
    else:
        print(f"\ntentativa de acesso de usuário não registrado detectada\nUsuário: {request.user}\n")
        return redirect("home")
