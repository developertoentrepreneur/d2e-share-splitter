from django import forms


class FormsUtils:
    def hide_field(self, field_name):
        self.fields[field_name].required = False
        self.fields[field_name].widget = forms.HiddenInput()


def choice_dynamic_field(choices):
    return forms.ChoiceField(
        choices=choices,
        widget=forms.Select(
            attrs={
                "onchange": "dynamicFormRequest();",
            }
        ),
    )
