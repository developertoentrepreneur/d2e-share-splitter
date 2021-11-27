from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers

from d2e_share_splitter.users.models import UserPie

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserPieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPie
        fields = [
            "name",
            "email",
            "jobTitle",
            "yearSalary",
        ]
