"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from data_collection.script import *
import json

class TwitterDataTestCase(TestCase):
	'''simple testcase to validate twitter api is worrking'''

	def setUp(self):
		username = 'mo_nearhan'
		count = 10
		self.spider = TwitterSpider(username, count)
		with open('test_data.json', 'r') as f:
			self.json_response = json.loads(f.read())

	def test_to_check_url_is_formated_correctly(self):
		url = self.spider.twitter_api_url
		match = re.match(r'\s', url)
		self.assertFalse(match)

	'''
	def test_to_check_parsing(self):
		data = self.spider.retrive_json()
		self.assertTrue(data)

	def test_to_return_error_when_no_tweets_found(self):
		spider = TwitterSpider('no_nearhan', 10)
		with self.assertRaises(TypeError):
			spider.retrive_json()
	'''

	def test_to_parse_single_tweet(self):
		single_tweet = self.json_response[0]

		print single_tweet.get('text')
		self.assertEquals("#-1 #headache writing this #program need a break", 
			single_tweet.get('text'))

		self.assertEquals(-1.0, self.spider.parse_mood_value(single_tweet))

		self.assertEquals(datetime(2013, 1, 8, 17, 59, 1), 
			self.spider.convert_date(single_tweet))

		# !! Not implemented as of yet
		#self.assertEquals('headache, program', 
		#	self.spider.parse_hash_tags(single_tweet))


	def test_to_parse_all_tweets_in_response(self):
		count = len(self.json_response)
		created_observations = self.spider.parse_json_into_models(self.json_response)
		self.assertEquals(count, len(created_observations))

		for observation in created_observations:
			print observation




		

