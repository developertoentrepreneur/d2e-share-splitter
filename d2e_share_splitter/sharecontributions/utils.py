from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework.generics import get_object_or_404

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.sharecontributions.models import ContributionTypeChoices


def compute_contrib_pie_slices(contrib: Contribution):
    project: Project = contrib.projectType
    if contrib.contribType == ContributionTypeChoices.time.name:
        hourly_rate = (
            contrib.user.yearSalary / 2000
        )  # since it's considered 2000h/year
        cash_amount = contrib.hours * hourly_rate
        slices = cash_amount * project.non_cash_multiplier

    elif contrib.contribType == ContributionTypeChoices.expenses.name:
        slices = contrib.amount * project.cash_multiplier

    contrib.slices = slices
    contrib.save(update_fields=["slices"])


def compute_user_pie_slices(user_id):
    User = get_user_model()
    user: User = get_object_or_404(User, user_id)
    user_contributions = Contribution.objects.filter(user=user)
    slices_user = user_contributions.aggregate(Sum("slices")).get("slices__sum")
    return slices_user
