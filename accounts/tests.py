from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from accounts.models import UserToken
from accounts.utils import cipher_suite


class UserAuthTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.user1 = User.objects.create_user(
			username='usuario_de_teste', password='Senha1234!'
		)

	def test_signup_view(self):
		response = self.client.post(
			'/accounts/signup/',
			{
				'username': 'claire',
				'password1': 'Cottrill1234',
				'password2': 'Cottrill1234',
			},
		)

		self.assertRedirects(response, reverse('token'))

	def test_token_view(self):
		self.client.force_login(self.user1)
		response = self.client.get('/accounts/token/')

		decrypted_token = cipher_suite.decrypt(
			self.user1.token.token.encode()  # type: ignore
		).decode()

		self.assertEqual(response.status_code, 200)
		self.assertEqual(decrypted_token, response.context['token'])

	def test_update_password_view(self):
		self.client.force_login(self.user1)
		response = self.client.post(
			'/accounts/update-password/',
			{
				'old_password': 'Senha1234!',
				'new_password1': 'NovaSenha1234!',
				'new_password2': 'NovaSenha1234!',
			},
		)

		self.assertRedirects(response, reverse('home'))
		self.user1.refresh_from_db()
		self.assertTrue(self.user1.check_password('NovaSenha1234!'))

	def test_reset_password_view(self):
		self.client.force_login(self.user1)
		response = self.client.post(
			'/accounts/reset-password/',
			{
				'new_password1': 'RedefinirSenha1234!',
				'new_password2': 'RedefinirSenha1234!',
			},
		)

		self.assertRedirects(response, reverse('home'))
		self.user1.refresh_from_db()
		self.assertTrue(self.user1.check_password('RedefinirSenha1234!'))

	def test_token_validation_view(self):
		user = User.objects.get(username=self.user1.username)  # type: ignore
		user_token = UserToken.objects.get(user=user)
		decrypted_token = cipher_suite.decrypt(user_token.token.encode()).decode()

		response = self.client.post(
			'/accounts/token-validation/',
			{
				'username': self.user1.username,
				'token': decrypted_token,  # type: ignore
			},
		)

		self.assertRedirects(response, reverse('reset-password'))
