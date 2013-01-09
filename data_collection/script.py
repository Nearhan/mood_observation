import requests, re
from data_collection.models import Observation, UserProfile
from datetime import datetime


#we will be importing other models evenutally

class TwitterSpider(object):
	''' an object that will retrieve twitter and process it '''

	def __init__(self, username, count=20):

		self.twitter_api_url = ('https://api.twitter.com/1/statuses/user_timeline.json?'
			'include_entities=true&include_rts=true&screen_name={username}&count={count}'.format(username=username, count=count))
		
		self.userProfile = UserProfile.get(twitter_name=username)
		self.username = self.userProfile.twitter_name
		self.tweet_count = count

	def retrive_json(self):
		response = requests.get(self.twitter_api_url)
		json = response.json()

		if 'errors' in json:
			raise TypeError('no tweets for that user, make sure you spelled username correctly')
		return json

	def parse_json_into_models(self, data):
		created_objects = []
		for tweet in data:
			text = tweet.get('text')
			mood_value = self.parse_mood_value(tweet)
			date = self.convert_date(tweet)

			new_observation = Observation(tweet=text, 
				mood_value=mood_value, date=date, twitter_user=self.username)
			created_objects.append(new_observation)
		return created_objects


	def save_all_observations(self, created_objects):
		for obs in created_objects:
			print 'saving obs'
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
		return datetime.strptime(date_str, '%a %b %d %H:%M:%S +0000 %Y')

	def parse_hash_tags(self, tweet):
		''' parse entities dict and reutrn a string of hash tags '''

		output = ''
		for tag in tweet.get('entities').get('hashtags'):
			output += tag.get('text') + ', '
			output = output.rstrip()

		return output





















