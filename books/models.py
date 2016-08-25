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


class Loan(models.Model):
    """Class represents lean book by reader"""

    loan_date = models.DateField()
    return_date = models.DateField()
    loan_status = models.IntegerField()

    class Meta:
        db_table = 'loan'


class Reservation(models.Model):
    """Class represents reservation"""

    reservation_date = models.DateField()
    reservation_status = models.DateField()

    class Meta:
        db_table = 'reservation'


class Item(models.Model):
    """Class represents book item"""

    loans = models.ForeignKey(Loan, blank=True, on_delete=models.CASCADE)
    available = models.BooleanField()

    class Meta:
        db_table = 'item'

<<<<<<< HEAD

class Book(models.Model):
    """Class represents book"""

    authors = models.ManyToManyField(Author, blank=True)
    items = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, )
    reservation = models.ForeignKey(Reservation, blank=True, null=True, on_delete=models.CASCADE)

    publisher = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    edition = models.IntegerField(blank=True, null=True)
    edition_date = models.DateField(blank=True, null=True)
    pages = models.IntegerField()
    available = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'book'

    def __unicode__(self):
        return self.title
=======
	loans = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
	available = models.BooleanField()
	
	class Meta:
		db_table = 'item'

class Book(models.Model):
	"""Class represents book"""

	authors = models.ManyToManyField(Author, blank=True)
	items = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, )
	reservation = models.ForeignKey(Reservation, blank=True, null=True, on_delete=models.CASCADE)

	publisher = models.CharField(max_length=50)
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
>>>>>>> b518e97fa62b22de730c4a08f333a5e8899137fc
