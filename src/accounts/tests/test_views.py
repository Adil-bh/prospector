import os
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application
from django.urls import reverse

#
os.environ['DJANGO_SETTINGS_MODULE'] = 'prospector.settings'
application = get_wsgi_application()
CustomUser = get_user_model()


class HomeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123"
        )

    def test_user_home_view(self):
        # Connexion en tant qu'utilisateur de test
        login_successful = self.client.login(username="testuser", password="testpassword123")
        self.assertTrue(login_successful)

        # Construire l'URL et faire une requête GET
        url = reverse("accounts:home")
        response = self.client.get(url)

        # Vérifier le statut de la réponse
        self.assertEqual(response.status_code, 200)

        # Vérifier que le template utilisé est le bon
        # print(response)
        # self.assertTemplateUsed(response, "home.html")