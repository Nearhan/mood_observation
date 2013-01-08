from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Observation(models.Model):
	tweet = models.CharField(max_length=140)
	mood_value = models.FloatField()
	twitter_user = models.CharField(max_length=30)
	#hash_tags = models.CharField(max_length=140)
	date = models.DateTimeField()


	def __unicode__(self):
		return 'Observation: {tweet}'.format(tweet=self.tweet)




