from django import forms

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.models import (
    ContributionTypeChoices,
)  # NOQA
from d2e_share_splitter.sharecontributions.models import (
    contribution_type_choices,
)  # NOQA
from d2e_share_splitter.users.models import User

fields_form_shareconribution = [
    "details",
    "user",
    "contribType",
    "projectType",
    "hours",
    "date",
]


class FormCreateContribution(forms.Form):
    details = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    contribType = forms.ChoiceField(
        choices=ContributionTypeChoices.choices(),
        widget=forms.Select(
            attrs={
                "onchange": "dynamicFormRequest();",
            }
        ),
    )
    projectType = forms.ModelChoiceField(
        queryset=Project.objects.all(),
    )
    hours = forms.TimeField()
    amount = forms.TimeField()
    date = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data:
            contribType = self.data.get("contribType")
            if contribType == ContributionTypeChoices.expenses.name:
                self.fields["hours"].required = False
                self.fields["hours"].widget = forms.HiddenInput()
