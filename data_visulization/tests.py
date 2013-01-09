"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class TestSignUpView(TestCase):
	''' Test the signup view '''

	def setUp(self):
		self.client = Client()


	def test_login_page_has_form(self):
		response = self.client.get('/signup')
		self.assertTemplateUsed(response, 'data_visulization/signup.html')