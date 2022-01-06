from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.models import Contribution


def get_project(project_id=None):
    if project_id:
        return get_object_or_404(Project, project_id)
    return Project.objects.first()


def compute_pie_slices(project_id=None):
    project = get_project(project_id)

    # user = User.objects.get(name=name)
    # if hours != 0:
    #     print("in hours: " + str(hours))
    #     hourly_rate = user.yearSalary / 2000  # since it's considered 2000h/year
    #     value = hours * hourly_rate
    #     slices = value * project.non_cash_multiplier
    #     print(
    #         "slices: "
    #         + str(slices)
    #         + ", hourlyrate: "
    #         + str(hourly_rate)
    #         + ", expenses: "
    #         + str(expenses)
    #         + ", Noncash: "
    #         + str(project.non_cash_multiplier)
    #         + ", value: "
    #         + str(value)
    #     )
    # elif expenses != 0:
    #     value = expenses
    #     slices = value * project.cash_multiplier

    # user.slices = user.slices + slices
    # user.save()

    slices = 100
    value = 100

    return {"slices": round(slices, 2), "value": round(value, 2)}


def compute_user_pie_slices(user_id):
    User = get_user_model()
    user: User = get_object_or_404(User, user_id)
    user_contributions = Contribution.objects.filter(user=user)
