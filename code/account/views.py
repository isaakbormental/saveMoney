from django.shortcuts import render
from django.utils import timezone
from .models import Bill, Position
from .aggregate_expense import AggregateExpense, Aggregator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.urls import reverse_lazy
from .forms import ExpenseForm
from django.http import HttpResponseRedirect


class ListExpensesView(LoginRequiredMixin, View):
    """Controller listing expenses"""

    template_name = 'account/expenses_list.html'

    def get(self, request):
        bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        aggregate = Aggregator.aggregate_expenses_by_date(bills)
        context = {'day_aggregates': aggregate}
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


class ExpenseCreateView(LoginRequiredMixin, View):
    """Controller for creating Candidate"""
    model = Bill
    template_name = 'account/expenses/create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses-list')

    def get(self, request, **kwargs):
        context = dict()
        context['form'] = ExpenseForm()
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.author = request.user
            expense.save()
            return HttpResponseRedirect(self.success_url)
        else:
            context = {'form': form}
            form.add_error(None, 'The form is incorrect')
            return render(request, self.template_name, context)


class StatsView(LoginRequiredMixin, View):
    """Controller for stats circle"""
    template_name = 'account/stats_circle.html'
    
    def get(self, request, **kwargs):
        context = dict()
        return render(request, self.template_name, context)