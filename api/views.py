from django.views.generic.base import View
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from django.db.models import Sum
import json

from account.models import Bill, CATEGORIES
from api.serializers import BillSerializer

class BillListView(ListAPIView):
    """
    List all bills
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class MonthsCatsView(View):
    """
    Get categores summary for a month
    """
    def get(self, request, **kwargs):
        bills = Bill.objects.filter()
        # aggregate = Aggregator.aggregate_expenses_by_date(bills)
        bills = Bill.objects.values('category').annotate(y=Sum('summa'))
        # context = {'day_aggregates': aggregate}
        bills = [{'label': obj['category'], 'y': obj['y']} for obj in list(bills)]
        return HttpResponse(json.dumps(list(bills)))
