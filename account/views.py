from django.shortcuts import render
from django.utils import timezone
from .models import Bill, Position
from .aggregate_expense import AggregateExpense
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View


# def expenses_list(request):
#     bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
#     aggregate = []
#     for bill in bills:
#         aggregate.append(AggregateExpense(bill))
#     return render(request, 'account/expenses_list.html', {'bills': aggregate})


class ListExpensesView(LoginRequiredMixin, View):
    """Controller listing bills"""

    template_name = 'account/expenses_list.html'

    def get(self, request):
        bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        aggregate = []
        context = {'bills': aggregate}
        for bill in bills:
            aggregate.append(AggregateExpense(bill))
        return render(request, self.template_name, context)
