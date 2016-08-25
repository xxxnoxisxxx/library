from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','name', 'surname')
	list_filter = ('surname',)
 

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

