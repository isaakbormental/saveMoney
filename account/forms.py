from .models import Bill
from django import forms


class ExpenseForm(forms.ModelForm):
    """ Form for Bill's Model """

    class Meta:
        model = Bill
        fields = '__all__'
        exclude = ['author']
