import factory
from factory.django import DjangoModelFactory

from d2e_share_splitter.shareconf.factories import ProjectFactory
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.sharecontributions.models import ContributionTypeChoices


class ContributionFactory(DjangoModelFactory):
    class Meta:
        model = Contribution

    project = factory.SubFactory(ProjectFactory)


class ContributionTime10hFactory(ContributionFactory):
    contribType = ContributionTypeChoices.time.name
    hours = 10
    date = factory.Faker("date")
