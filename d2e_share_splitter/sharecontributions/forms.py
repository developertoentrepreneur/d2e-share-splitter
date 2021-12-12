from django import forms

from d2e_share_splitter.shareconf.models import Project
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
        choices=contribution_type_choices,
    )
    projectType = forms.ModelChoiceField(
        queryset=Project.objects.all(),
    )
    hours = forms.TimeField()
    date = forms.DateField()
