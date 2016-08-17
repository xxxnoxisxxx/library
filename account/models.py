from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
	"""Class represents Author"""

	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)


class Loan(models.Model):
	"""Class represents lean book by reader"""

	loan_date = models.DateField()
	return_date = models.DateField()
	loan_status = models.IntegerField()


class Reservation(models.Model):
	"""Class represents reservation"""

	reservation_date = models.DateField()
	reservation_status = models.DateField()


class Item(models.Model):
	"""Class represents book item"""

	loans = models.ForeignKey(Loan, blank=True)

	available = models.BooleanField()


class Reader(models.Model):
	"""Class represents reader"""
	reader = models.OneToOneField(User, on_delete=models.CASCADE)
	loans = models.ForeignKey(Loan, blank=True, null=True)

	id_card = models.CharField(max_length=9, unique=True)
	mobile = models.CharField(max_length=50)


	def __unicode__(self):
		return '%s %s' % (reader.last_name, reader.first_name)

	class Meta:
		db_table = 'reader'
		ordering = ['reader']


class Book(models.Model):
	"""Class represents book"""

	authors = models.ManyToManyField(Author, blank=True)
	items = models.ForeignKey(Item, blank=True)
	reservation = models.ForeignKey(Reservation, blank=True)

	id_book = models.IntegerField(primary_key=True)
	publisher = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	isbn = models.IntegerField()
	edition = models.IntegerField()
	edition_date = models.DateField()
	pages = models.IntegerField()
	available = models.IntegerField()	



		

		




		