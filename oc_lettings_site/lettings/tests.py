from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=48,
            street="rue du lac",
            city="Créteil",
            state="Val de marne",
            zip_code=94000,
            country_iso_code="fra"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Lettings</title>")

    def test_letting_detail(self):
        url = reverse('lettings:letting', args=[self.letting.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"<title>{self.letting.title}</title>")
