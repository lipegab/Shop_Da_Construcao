from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase

from .models import BlogTip, Offer, Partner


class PublicPagesTests(TestCase):
    def test_all_public_pages_render(self):
        for path in (
            "/",
            "/ofertas/",
            "/trabalhe-conosco/",
            "/blog/",
            "/marcas-parceiras/",
        ):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_homepage_displays_active_database_content(self):
        today = date.today()
        Offer.objects.create(
            name="Cimento teste",
            price=Decimal("39.90"),
            valid_from=today - timedelta(days=1),
            valid_until=today + timedelta(days=1),
        )
        BlogTip.objects.create(
            title="Dica de teste",
            category="Materiais",
            content="Conteúdo para o teste.",
            published=True,
        )
        Partner.objects.create(name="Marca teste", category="Tintas")

        response = self.client.get("/")

        self.assertContains(response, "Cimento teste")
        self.assertContains(response, "Dica de teste")
        self.assertContains(response, "Marca teste")

    def test_inactive_or_expired_records_are_not_public(self):
        today = date.today()
        Offer.objects.create(
            name="Oferta expirada",
            price=Decimal("10.00"),
            valid_from=today - timedelta(days=5),
            valid_until=today - timedelta(days=1),
        )
        BlogTip.objects.create(
            title="Rascunho privado",
            category="Teste",
            content="Não publicar.",
            published=False,
        )
        Partner.objects.create(
            name="Parceiro inativo",
            category="Teste",
            active=False,
        )

        for path in ("/", "/ofertas/"):
            with self.subTest(path=path):
                self.assertNotContains(self.client.get(path), "Oferta expirada")
        self.assertNotContains(self.client.get("/blog/"), "Rascunho privado")
        self.assertNotContains(self.client.get("/marcas-parceiras/"), "Parceiro inativo")
