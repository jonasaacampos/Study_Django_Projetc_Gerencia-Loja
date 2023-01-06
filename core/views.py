from django.shortcuts import render
from django.contrib import messages

from core.forms import ContatoForm, ProdutoModelForm


def dev_show_data_product_pre_save(produto):
    print(f"""
     nome: {produto.nome}\n
     preço: {produto.preco}\n
     estoque: {produto.estoque}\n
     imagem: {produto.imagem}
     """)


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
    if str(request.method) == "POST":
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            dev_show_data_product_pre_save(prod)
            messages.success(request, "Produto salvo com sucesso.")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Erro ao salvar... tente novamente após alguns minutos")

    else:
        form = ProdutoModelForm()
    context = {
        "form": form
    }
    return render(request, "produto.html", context)
