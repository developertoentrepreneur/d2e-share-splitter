from typing import Any
from typing import Dict

from django import forms

from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.sharecontributions.utils import compute_pie_slices


class FormCreateContribution(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = [
            "contribType",
            "projectType",
            "value",
            "hours",
            "date",
            "details",
            "slices",
        ]

    def clean(self) -> Dict[str, Any]:
        clean = super().clean()
        # compute_pie_slices(self.user, expenses, hours)
        return clean
