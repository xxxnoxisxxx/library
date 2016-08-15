from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reader(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	id_card = models.CharField(max_length=9, unique=True)
	mobile = models.CharField(max_length=50)

	def __unicode__(self):
		return '%s %s' % (user.last_name, user.first_name)

	class Meta:
		db_table = 'reader'
		ordering = ['user']