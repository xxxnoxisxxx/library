from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
	"""Class represents Author"""

	name = models.CharField(max_length=35)
	surname = models.CharField(max_length=35)
		
	class Meta:
		db_table = 'author'

	def __unicode__(self):
		return '%s %s' % (self.name, self.surname)

class Publisher(models.Model):
	"""Class represents publisher"""

	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Book(models.Model):
	"""Class represents book"""

	authors = models.ManyToManyField(Author, blank=True)
	publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.CASCADE)

	title = models.CharField(max_length=50)
	isbn = models.CharField(max_length=20)
	edition = models.IntegerField(blank=True, null=True)
	edition_date = models.DateField(blank=True, null=True)
	pages = models.IntegerField()
	description = models.TextField()
	
	class Meta:
		db_table = 'book'

	def __unicode__(self):
		return self.title 

class Item(models.Model):
	"""Class represents book item"""

	books = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
	available = models.BooleanField(default=True)
	
	class Meta:
		db_table = 'item'

	def __unicode__(self):
		return self.books.title

class Reservation(models.Model):
	"""Class represents reservation"""
	books = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
	
	reservation_date = models.DateField()
	reservation_status = models.IntegerField(default=7)
	
	class Meta:
		db_table = 'reservation'

	def __unicode__(self):
		return str(self.id) + " " + self.books.title 
	
class Loan(models.Model):
	"""Class represents lean book by reader"""
	items = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE)

	loan_date = models.DateField()
	return_date = models.DateField()
	loan_status = models.IntegerField()
	
	class Meta:
		db_table = 'loan'

	def __unicode__(self):
		return self.items.books.name + str(self.loan_date) + str(self.return_date)
