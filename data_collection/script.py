import requests, re
from data_collection.models import Observation, UserProfile
from datetime import datetime, timedelta
from django.contrib.auth.models import User


#we will be importing other models evenutally

class TwitterSpider(object):
	''' an object that will retrieve twitter and process it '''

	def __init__(self, username, count=200):
		self.user = User.objects.get(username=username)
		try:
			self.userProfile = self.user.userprofile
		except UserProfile.DoesNotExist:
			print 'set up a user profile'

		self.twitter_username = self.userProfile.twitter_username
		self.tweet_count = count
		self.twitter_api_url = self.get_twitter_api_url(self.twitter_username, self.tweet_count)

	def get_twitter_api_url(self, username, count):
		url = ('https://api.twitter.com/1/statuses/user_timeline.json?'
			'include_entities=true&include_rts=true&screen_name={username}&count={count}')
		return url.format(username=username, count=count)


	def retrive_json(self):
		response = requests.get(self.twitter_api_url)
		json = response.json()

		if 'errors' in json:
			raise TypeError('no tweets for that user, make sure you spelled username correctly')
		return json


	def parse_json_into_models(self, data):
		created_objects = []

		data = self.return_newest_tweets(data)

		for tweet in data:
			text = tweet.get('text')
			mood_value = self.parse_mood_value(tweet)
			date = self.convert_date(tweet)
			tweet_id = self.get_tweet_id(tweet)
			user = UserProfile.objects.get(twitter_username=self.twitter_username)

			new_observation = Observation(tweet=text, 
				mood_value=mood_value, date=date, user=user, tweet_id=tweet_id)
			created_objects.append(new_observation)
		return created_objects


	def get_tweet_id(self, tweet):
		return tweet.get('id')


	def save_all_observations(self, created_objects):
		for obs in created_objects:
			obs.save()


	def parse_mood_value(self, tweet):
		''' will parse out value hash tag and convert it to a float '''
		text = tweet.get('text')
		value_string = re.findall(r'#-\d+|#\d+', text)[0]
		integer = value_string.split('#')[1]
		return float(integer)


	def convert_date(self, tweet):
		'''will return date in proper format'''
		date_str = tweet.get('created_at')
		date_str = date_str.replace('+0000', '')
		date = datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')
		correct_date = date + timedelta(hours=-5)
		return correct_date


	def parse_hash_tags(self, tweet):
		''' parse entities dict and reutrn a string of hash tags '''

		output = ''
		for tag in tweet.get('entities').get('hashtags'):
			output += tag.get('text') + ', '
			output = output.rstrip()
		return output


	def return_newest_tweets(self, json):
		''' queries db for latests observation 
		and constructs new json object to pass on new observation models'''

		try:
			latest = Observation.objects.get_latest(self.userProfile)

		except Observation.DoesNotExist:
			print 'No exsisting observations'
			return json

		for index, tweet in enumerate(json):

			if tweet.get('id') == latest.tweet_id:
				return json[:index]
						

	def start(self):
		''' convience wrapper for spider to retrive json and create objects'''
		#retrive data
		data = self.retrive_json()

		#parse data into models
		observations = self.parse_json_into_models(data)

		#save all observations models to db
		self.save_all_observations(observations)

		return observations















