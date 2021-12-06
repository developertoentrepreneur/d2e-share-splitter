from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.users.models import User


def update_pie_slices():
    users = Contribution.get_users()
    for user_name in users:
        try:
            user = User.objects.get(name=user_name)
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
