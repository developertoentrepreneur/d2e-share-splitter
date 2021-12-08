from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.users.forms import User


def compute_pie_slices(
    name,
    expenses=0,
    hours=None,
):
    project = Project.objects.first()
    user = User.objects.get(name=name)
    if hours != 0:
        print("in hours: " + str(hours))
        hourly_rate = user.yearSalary / 2000  # since it's considered 2000h/year
        value = hours * hourly_rate
        slices = value * project.non_cash_multiplier
        print(
            "slices: "
            + str(slices)
            + ", hourlyrate: "
            + str(hourly_rate)
            + ", expenses: "
            + str(expenses)
            + ", Noncash: "
            + str(project.non_cash_multiplier)
            + ", value: "
            + str(value)
        )
    elif expenses != 0:
        value = expenses
        slices = value * project.cash_multiplier

    user.slices = user.slices + slices
    user.save()

    return {"slices": round(slices, 2), "value": round(value, 2)}
