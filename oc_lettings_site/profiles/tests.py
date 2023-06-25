from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="TestUser", password="TestPass")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_index(self):
        url = reverse("profiles:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, self.profile.user)

    def test_profile_detail(self):
        url = reverse("profiles:profile", args=[self.profile.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertEqual(response.context["profile"], self.profile)
