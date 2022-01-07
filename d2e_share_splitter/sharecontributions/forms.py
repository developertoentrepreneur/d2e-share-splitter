from django import forms

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.models import (
    ContributionTypeChoices,
)  # NOQA
from d2e_share_splitter.sharecontributions.models import (
    contribution_type_choices,
)  # NOQA
from d2e_share_splitter.users.models import User
from d2e_share_splitter.utils.form_utils import FormsUtils
from d2e_share_splitter.utils.form_utils import choice_dynamic_field

fields_form_shareconribution = [
    "details",
    "user",
    "contribType",
    "projectType",
    "hours",
    "date",
]


class FormCreateContribution(forms.Form, FormsUtils):
    details = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    contribType = choice_dynamic_field(ContributionTypeChoices.choices())
    projectType = forms.ModelChoiceField(
        queryset=Project.objects.all(),
    )
    hours = forms.TimeField()
    amount = forms.FloatField()
    date = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data:
            self.toggle_hours_or_amount()

    def toggle_hours_or_amount(self):
        contribType = self.data.get("contribType")
        if contribType == ContributionTypeChoices.expenses.name:
            self.hide_field("hours")
        elif contribType == ContributionTypeChoices.time.name:
            self.hide_field("amount")
