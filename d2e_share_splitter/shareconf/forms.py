from django import forms

from d2e_share_splitter.shareconf.models import Project


class FormCreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "cash_multiplier", "non_cash_multiplier"]
