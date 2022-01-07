from allauth.account.models import EmailAddress

from d2e_share_splitter.users.tests.factories import TokenUserFactory


def create_admin_user():
    data = {
        "user__username": "admin",
        "user__email": "admin@fake.com",
        "user__is_staff": True,
        "user__is_active": True,
        "user__password": "admin",
    }
    token = TokenUserFactory(**data)
    verify_user(token.user)

    return token.user


def verify_user(user):
    account, _ = EmailAddress.objects.get_or_create(user=user, email=user.email)
    account.verified = True
    account.primary = True
    account.save()
