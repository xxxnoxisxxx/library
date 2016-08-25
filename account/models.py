from __future__ import unicode_literals
from django.core.validators import RegexValidator

from django.contrib.auth.models import User
from django.db import models

from books.models import Loan, Reservation


class Reader(models.Model):
    """Class represents reader"""
    reader = models.OneToOneField(User, on_delete=models.CASCADE)
    loans = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, blank=True, null=True, on_delete=models.CASCADE)

    id_card = models.CharField(max_length=9, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(max_length=50, validators=[phone_regex], blank=True)

    class Meta:
        db_table = 'reader'

    def __unicode__(self):
        return '%s %s' % (self.reader.last_name, self.reader.first_name)
