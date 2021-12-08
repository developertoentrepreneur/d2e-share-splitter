from d2e_share_splitter.shareconf.models import ShareConfiguration
from d2e_share_splitter.users.forms import User


def compute_pie_slices(
    name,
    expenses=0,
    hours=None,
):
    shareconf = ShareConfiguration.objects.get(pk=1)
    user = User.objects.get(name=name)
    if hours != 0:
        print("in hours: " + str(hours))
        hourly_rate = user.yearSalary / 2000  # since it's considered 2000h/year
        value = hours * hourly_rate
        slices = value * shareconf.nonCashMultiplier
        print(
            "slices: "
            + str(slices)
            + ", hourlyrate: "
            + str(hourly_rate)
            + ", expenses: "
            + str(expenses)
            + ", Noncash: "
            + str(shareconf.nonCashMultiplier)
            + ", value: "
            + str(value)
        )
    elif expenses != 0:
        value = expenses
        slices = value * shareconf.cashMultiplier

    user.slices = user.slices + slices
    user.save()

    return {"slices": round(slices, 2), "value": round(value, 2)}
