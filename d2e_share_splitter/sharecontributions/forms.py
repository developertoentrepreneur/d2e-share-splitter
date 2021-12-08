from typing import Any
from typing import Dict

from django import forms

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.sharecontributions.utils import compute_pie_slices
from d2e_share_splitter.users.models import User

contribution_type_choices = (
    ("time", "Time"),
    ("expenses", "Expenses"),
)


class FormCreateContribution(forms.ModelForm):
    details = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    contribType = forms.ChoiceField(
        choices=contribution_type_choices,
    )
    projectType = forms.ModelChoiceField(
        queryset=Project.objects.all(),
    )
    hours = forms.TimeField()
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Contribution
        fields = [
            "details",
            "user",
            "contribType",
            "projectType",
            "value",
            "hours",
            "date",
        ]

    def clean(self) -> Dict[str, Any]:
        clean = super().clean()
        # compute_pie_slices(self.user, expenses, hours)
        return clean
