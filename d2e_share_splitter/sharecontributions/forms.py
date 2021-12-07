from django import forms

from d2e_share_splitter.sharecontributions.models import Contribution


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
