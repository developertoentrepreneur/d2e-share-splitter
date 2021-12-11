from rest_framework import serializers

from d2e_share_splitter.sharecontributions.models import Contribution


class ContributionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = [
            "details",
            "user",
            "contribType",
            "projectType",
            "value",
            "hours",
            "date",
        ]
