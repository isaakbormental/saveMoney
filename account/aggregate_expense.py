from django.utils import timezone
from .models import Bill, Position

class AggregateExpense:

    def __init__(self, bill):
        self.bill = bill
        self.positions = Position.objects.filter(bill_id_id=bill.id)
