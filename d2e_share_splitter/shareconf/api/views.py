from django.urls import reverse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.utils.views_modal import ModalRetrieveUpdateView

from .serializers import ProjectFormSerializer


class ProjectRetrieveUpdateView(ModalRetrieveUpdateView):
    queryset = Project.objects.all()
    serializer_class = ProjectFormSerializer
    lookup_url_kwarg = "project_pk"
    redirect_url = "shareconf:pie_conf"

    def get(self, request, project_pk):
        project: Project = get_object_or_404(Project, pk=project_pk)
        response = {
            "project": project,
            "serializer": self.get_serializer(project),
            "url_edit": reverse("shareconf:form", kwargs={"project_pk": project.pk}),
            "title": f"Update project {project.name}",
        }
        return Response(response)
