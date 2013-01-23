from django.core.management.base import BaseCommand, CommandError
from data_collection.script import TwitterSpider
from django.contrib.auth.models import User



class Command(BaseCommand):
	args = '<username>'
	help = 'Grabs tweets of user'

	def handle(self, username, **options):

		try:
			spider = TwitterSpider(username)
		except User.DoesNotExist:
			raise CommandError('User does not exsit in system')

		#start the spider
		observations = spider.start()

		if observations:
			for observation in observations:
				self.stdout.write('New Tweet: {0} \n '.format(observation.tweet))

		else:
			self.stdout.write('No new tweets for {0} \n '.format(username))