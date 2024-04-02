from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UsedTestCase(TestCase):
    def setUp(self):
        pass

    def test_main_page(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(response.context_data['title'], 'Главная страница')

    def tearDown(self):
        pass


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            'username': 'knight',
            'email': 'testtest@gmail.com',
            'password1': 'ZxjEI178Aa',
            'password2': 'ZxjEI178Aa',
        }

    def test_registration(self):
        path = reverse('register')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_registration_success(self):
        user_model = get_user_model()

        path = reverse('register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(
            user_model.objects.filter(username=self.data['username']).exists())

    def test_registration_password_error(self):
        self.data['password2'] = 'rewiri3oo4'
        path = reverse('register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Введенные пароли не совпадают')

    def test_registration_user_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create(username=self.data['username'])
        path = reverse('register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response,
                            'Пользователь с таким именем уже существует')
