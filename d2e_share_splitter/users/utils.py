from d2e_share_splitter.users.tests.factories import TokenUserFactory


def create_admin_user():
    data = {
        "user__username": "admin",
        "user__email": "admin@fake.com",
        "user__is_staff": True,
    }
    token = TokenUserFactory(**data)
    return token.user
