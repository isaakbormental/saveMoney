from django.utils import timezone
from .models import Bill, Position


class AggregateExpense:

    def __init__(self, bill):
        self.bill = bill
        self.positions = Position.objects.filter(bill_id_id=bill.id)


class DayAggregate:
    def __init__(self, date):
        self.date = date
        self.total = 0.0
        self.expenses = []
        # self.day_expenses = Bill.objects.filter(created_date=date).order_by('created_date')

    def put_expense(self, expense):
        self.expenses.append(expense)


class Aggregator:
    @staticmethod
    def aggregate_expenses_by_date(expenses):
        viewed_dates = set()
        aggregate_result = []
        for obj in expenses:
            if obj.created_date not in viewed_dates:
                viewed_dates.add(obj.created_date)
                new_expense = DayAggregate(obj.created_date)
                new_expense.put_expense(obj)
                new_expense.total += obj.summa
                aggregate_result.append(new_expense)
            else:
                aggregate_result[-1].put_expense(obj)
                aggregate_result[-1].total += obj.summa
        return aggregate_result
