from django.core.validators import MinValueValidator
from django.db import models


class Offer(models.Model):
    name = models.CharField("produto", max_length=150)
    description = models.TextField("descrição", blank=True)
    image = models.ImageField("imagem", upload_to="offers/", blank=True)
    price = models.DecimalField(
        "preço",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    valid_from = models.DateField("início da oferta")
    valid_until = models.DateField("fim da oferta")
    active = models.BooleanField("ativa", default=True)

    class Meta:
        ordering = ("valid_until", "name")
        verbose_name = "oferta"
        verbose_name_plural = "ofertas"

    def __str__(self):
        return self.name


class BlogTip(models.Model):
    title = models.CharField("título", max_length=180)
    category = models.CharField("categoria", max_length=80)
    summary = models.CharField("resumo", max_length=300, blank=True)
    content = models.TextField("conteúdo")
    image = models.ImageField("imagem", upload_to="tips/", blank=True)
    published = models.BooleanField("publicada", default=False)
    created_at = models.DateTimeField("criada em", auto_now_add=True)

    class Meta:
        ordering = ("-created_at", "title")
        verbose_name = "dica"
        verbose_name_plural = "dicas"

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField("marca", max_length=120)
    category = models.CharField("categoria", max_length=100)
    logo = models.ImageField("logotipo", upload_to="partners/", blank=True)
    website = models.URLField("site", blank=True)
    active = models.BooleanField("ativa", default=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "marca parceira"
        verbose_name_plural = "marcas parceiras"

    def __str__(self):
        return self.name
