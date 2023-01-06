# todos os formulários devem ser criados dentro deste arquivo
from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto
class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50)
    email = forms.EmailField(label="Email", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=120)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea(), min_length=50)

    def send_mail(self):
        nome = self.cleaned_data["nome"]
        email = self.cleaned_data["email"]
        assunto = self.cleaned_data["assunto"]
        mensagem = self.cleaned_data["mensagem"]

        message_content = f"""
        Nome: {nome}\n
        email: {email}\n
        assunto: {assunto}\n
        mensagem:\n {mensagem}
        """

        mail = EmailMessage(
            subject=assunto + "Backend mail test...",
            body=message_content,
            from_email="contato@seudominio.org.br",
            to=["contato@seuEmail.com.br"],
            headers={"Responder para": email}
        )

        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco", "estoque", "imagem"]
