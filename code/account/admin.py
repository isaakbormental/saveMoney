from django.contrib import admin
from .models import Bill
from .models import Position

admin.site.register(Bill)
admin.site.register(Position)