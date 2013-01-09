from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	twitter_username = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return 'User Profile of User {user}'.format(user=self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)


class Observation(models.Model):
	tweet = models.CharField(max_length=140)
	mood_value = models.FloatField()
	user = models.ForeignKey(UserProfile)
	#hash_tags = models.CharField(max_length=140)
	date = models.DateTimeField()


	def __unicode__(self):
		return 'Observation: {tweet}'.format(tweet=self.tweet)





