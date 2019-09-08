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
        bills = Bill.objects.values('category').annotate(y=Sum('summa'))
        bills = [{'label': obj['category'], 'y': obj['y']} for obj in list(bills)]
        return HttpResponse(json.dumps(list(bills)))
