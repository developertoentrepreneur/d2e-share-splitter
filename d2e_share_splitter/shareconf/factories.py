from factory.django import DjangoModelFactory

from d2e_share_splitter.shareconf.models import Project


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project


class NamedProjectFactory(ProjectFactory):
    name = "Pecunia"
