from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	twitter_username = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return 'User Profile of User {user}'.format(user=self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, raw=True, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
	profile = UserProfile.objects.get(user=instance)
	profile.delete()



class ObservationManager(models.Manager):

	def get_latest(self, user):
		return self.filter(user=user).latest('date')
		
		
class Observation(models.Model):
	tweet = models.CharField(max_length=140)
	mood_value = models.FloatField()
	user = models.ForeignKey(UserProfile)
	#hash_tags = models.CharField(max_length=140)
	date = models.DateTimeField()
	tweet_id = models.BigIntegerField(default=1, blank=True)

	objects = ObservationManager()


	def __unicode__(self):
		return 'Observation: {tweet}'.format(tweet=self.tweet)





