import os

from django.core.wsgi import get_wsgi_application
from django.test import TestCase
from django.contrib.auth import get_user_model

#
os.environ['DJANGO_SETTINGS_MODULE'] = 'prospector.settings'
application = get_wsgi_application()

# Obtenir le modèle CustomUser
CustomUser = get_user_model()


class TestCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Créer des données non modifiées pour tous les tests de la classe.")
        cls.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def setUp(self):
        self.user.refresh_from_db()

    def test_user_creation(self):
        print("Method: test_user_creation.")
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword123'))

    def test_unique_username(self):
        print("Method: test_unique_username.")
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                username='testuser',
                email='email.test@example.com',
                password='testpassword123')

    # def test_numeric_only_username(self):
    #     print("Method: test_numeric_only_username.")
    #     with self.assertRaises(Exception):
    #         CustomUser.objects.create_user(
    #             username='123456',
    #             email="testemail@example.fr",
    #             password='testpassword123')