from django.shortcuts import render
from django.utils import timezone
from .models import Bill, Position
from .aggregate_expense import AggregateExpense

def expenses_list(request):
    bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    aggregate = []
    for bill in bills:
        aggregate.append(AggregateExpense(bill))
    return render(request, 'account/expenses_list.html', {'bills': aggregate})
