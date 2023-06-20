from django.test import TestCase
from django.urls import reverse

def test_dummy():
    assert 1

class HomePageTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Holiday Homes</title>")


