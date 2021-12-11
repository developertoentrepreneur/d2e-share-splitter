from django.contrib.auth import get_user_model
from rest_framework import serializers

from d2e_share_splitter.users.models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "jobTitle",
            "yearSalary",
        ]
