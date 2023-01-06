from django.db import models
from stdimage import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    created_at = models.DateField("Data criação", auto_now=True)
    modified = models.DateField("Data alteração", auto_now=True)
    active = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preço", max_digits=5, decimal_places=2)
    estoque = models.IntegerField("Estoque")
    imagem = StdImageField(
        "imagem", upload_to="produtos", variations={"thumb": (125, 125)}
    )
    slug = models.SlugField("slug", max_length=100, blank=True, editable=False)


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
