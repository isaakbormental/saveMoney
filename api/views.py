from rest_framework.generics import ListAPIView

from account.models import Bill
from api.serializers import BillSerializer

class BillListView(ListAPIView):
    """
    List all bills
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
