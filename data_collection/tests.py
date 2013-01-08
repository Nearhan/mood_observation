"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from data_collection.script import TwitterSpider

class TwitterDataTestCase(TestCase):
	'''simple testcase to validate twitter api is worrking'''

	def setUp(self):
		pass


	def test_to_check_parsing(self):
		username = 'mo_nearhan'
		count = 10
		self.TwitterSpider = TwitterSpider(username, count)
		json = self.TwitterSpider.retrive_json()
		self.assertTrue(json)
		self.assertEquals(len(json), count)
		

