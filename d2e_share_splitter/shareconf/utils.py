from sharecontributions.models import Contribution
from shareusers.models import UserPie


def update_pie_slices():
    users = Contribution.get_users()
    for user_name in users:
        try:
            user = UserPie.objects.get(name=user_name)
        except Exception as e:
            print(e)
            return

        contributions_user = Contribution.objects.filter(user=user_name)
        slices = 0
        for contrib in contributions_user:
            slices += contrib.slices
        user.slices = slices
        user.save()

    print(users)
