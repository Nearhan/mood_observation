import requests, re


#we will be importing other models evenutally

class TwitterSpider(object):
	''' an object that will retrieve twitter and process it '''

	def __init__(self, username, count):

		self.twitter_api_url = 'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name={username}&count={count}'.format(username=username, count=count)

	def retrive_json(self):
		response = requests.get(self.twitter_api_url)
		if response.ok:
			json = response.json()
			return json

	def parse_json_into_models(self, model):
		pass

			# do more analysis here

