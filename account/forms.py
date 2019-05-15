from .models import Bill
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML


class ExpenseForm(forms.ModelForm):
    """ Form for Candidate's Model from human_resources """
    class Meta:
        model = Bill
        fields = '__all__'
        # exclude = ['hr', 'cv']
        # widgets = {
        #     'cv_text': forms.Textarea(attrs={'rows': 6}),
        #     'description': forms.Textarea(attrs={'rows': 6}),
        #     'birthdate': forms.widgets.DateInput(attrs={'type': 'date'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_helper = FormHelper()
        self.create_helper = FormHelper()
        self.update_helper = FormHelper()

        self.base_helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column('place', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'summa',
        )

        self.create_helper.layout = Layout(
            self.base_helper.layout,
            HTML("""
                <input type="submit" class="btn btn-outline-success btn-sm" value="Create">
                """)
        )

        self.update_helper.layout = Layout(
            self.base_helper.layout,
            HTML("""
                <input type="submit" class="btn btn-outline-success btn-sm" value="Update">
                """)
        )
