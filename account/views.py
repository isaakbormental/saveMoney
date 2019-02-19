from django.shortcuts import render
from django.utils import timezone
from .models import Bill, Position

def expenses_list(request):
    bills = Bill.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'account/expenses_list.html', {'bills': bills})
