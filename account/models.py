from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from books.models import Loan, Reservation


class Reader(models.Model):
    """Class represents reader"""
    reader = models.OneToOneField(User, on_delete=models.CASCADE)
    loans = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, blank=True, null=True, on_delete=models.CASCADE)

    id_card = models.CharField(max_length=9, unique=True)
    mobile = models.CharField(max_length=50)

    class Meta:
        db_table = 'reader'

    def __unicode__(self):
        return '%s %s' % (self.reader.last_name, self.reader.first_name)


class LibraryUser(models.Model):
    """Class represents library user"""
    username = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30, blank=False)
    password2 = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
