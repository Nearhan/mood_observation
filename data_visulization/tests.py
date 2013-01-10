"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from data_visulization.forms import SignupForm
from data_visulization.models import UserProifle

class TestSignUpView(TestCase):
	''' Test the signup view '''

	def setUp(self):
		self.client = Client()


	def test_to_check_template(self):
		response = self.client.get('/signup/')
		self.assertTemplateUsed(response, 'data_visulization/signup.html')



	def test_invalid_password_signup(self):
		invalid_data = {'username': 'asdf',
						'password': 'asdf',
						'verify_password': 'asde',
						'twitter_name': 'mo_nearhan'}

		response = self.client.post('/signup/', invalid_data)
		self.assertTrue('passwords do not match' in response.content)


	def test_to_check_user_is_created_after_form_submission(self):
		valid_data = {'username': 'asdf',
						'password': 'asdf',
						'verify_password': 'asdef',
						'twitter_name': 'mo_nearhan'}

		form = SignupForm(valid_data)

		self.assertEquals(form.new_user, 'asdf')








