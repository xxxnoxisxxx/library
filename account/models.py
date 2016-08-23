from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from books.models import Loan, Reservation


class Reader(models.Model):
	"""Class represents reader"""
	reader = models.OneToOneField(User, on_delete=models.CASCADE)
	loans = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
	reservation = models.ForeignKey(Reservation, blank=True,null=True, on_delete=models.CASCADE)

	id_card = models.CharField(max_length=9, unique=True)
	mobile = models.CharField(max_length=50)

	class Meta:
		db_table = 'reader'

	def __unicode__(self):
		return '%s %s' % (reader.last_name, reader.first_name)



		

		




		
