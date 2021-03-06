from __future__ import unicode_literals
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from account.models import Reader
from django.core.urlresolvers import reverse
from django.utils.timezone import now


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

    authors = models.ManyToManyField(Author, blank=False)
    publisher = models.ForeignKey(Publisher, blank=False, null=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    edition = models.IntegerField(blank=True, null=True)
    edition_date = models.DateField(blank=False, null=True)
    pages = models.IntegerField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('book_update', args=[self.id])

    class Meta:
        db_table = 'book'

    def __unicode__(self):
        return "%s, Edition: %s" %(self.title, self.edition)


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
    readers = models.ForeignKey(Reader, blank=True, null=True, on_delete=models.CASCADE)

    reservation_date = models.DateField()
    reservation_status = models.IntegerField(default=7)

    class Meta:
        db_table = 'reservation'

    def __unicode__(self):
        return "%s %s" % (self.id, self.books.title)


class Loan(models.Model):
    """Class represents lean book by reader"""
    items = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE)
    readers = models.ForeignKey(Reader, blank=True, null=True, on_delete=models.CASCADE)

    loan_date = models.DateTimeField(auto_now = True)
    return_date = models.DateTimeField(default=now()+timedelta(days=30), editable = False)

    class Meta:
        db_table = 'loan'

    def __unicode__(self):
        return "%s [%s] [%s]" % (self.items.books.title, self.loan_date.strftime("%Y-%m-%d %H:%M"), self.return_date.strftime("%Y-%m-%d %H:%M"))

