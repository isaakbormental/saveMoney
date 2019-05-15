from django.shortcuts import render
from django.utils import timezone
from .models import Bill, Position
from .aggregate_expense import AggregateExpense, Aggregator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View


class ListExpensesView(LoginRequiredMixin, View):
    """Controller listing expenses"""

    template_name = 'account/expenses_list.html'

    def get(self, request):
        bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        print(type(bills))
        print(bills)
        aggregate = Aggregator.aggregate_expenses_by_date(bills)

        # aggregate = []
        context = {'day_aggregates': aggregate}
        # for bill in bills:
        #     aggregate.append(AggregateExpense(bill))
        return render(request, self.template_name, context)


class ListExpensesWithPositionsView(LoginRequiredMixin, View):

    template_name = 'account/positions_list.html'

    def get(self, request):
        bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        aggregate = []
        context = {'bills': aggregate}
        for bill in bills:
            aggregate.append(AggregateExpense(bill))
        return render(request, self.template_name, context)
