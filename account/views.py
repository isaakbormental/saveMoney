from django.shortcuts import render

def expenses_list(request):
    return render(request, 'account/expenses_list.html', {})
