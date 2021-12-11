from rest_framework import serializers

from d2e_share_splitter.shareconf.models import Project


class ProjectFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "name",
            "cash_multiplier",
            "non_cash_multiplier",
        ]
