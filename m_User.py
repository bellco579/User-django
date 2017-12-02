from django.db import models
from project.models import *
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	test = models.CharField(max_length=30)
	user = models.OneToOneField(User, unique=True, related_name='profile')
	project = models.ForeignKey(project,blank=True,null=True,default=None)
	objects = UserManager()

	class Meta:
		db_table = 'profiles'
		verbose_name = 'user profile'
		verbose_name_plural = 'user profiles'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
