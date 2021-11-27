from typing import Any
from typing import Sequence

import factory
from django.contrib.auth import get_user_model
from factory import Faker
from factory import post_generation
from factory.django import DjangoModelFactory
from rest_framework.authtoken.models import Token

from d2e_share_splitter.users.models import UserPie


class UserFactory(DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class TokenUserFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Token
        django_get_or_create = ("user",)


class UserPieFactory(DjangoModelFactory):
    class Meta:
        model = UserPie

    name = "Default User"
    email = "default@mail.com"
    jobTitle = "Admin"
    yearSalary = 123
    slices = 0
