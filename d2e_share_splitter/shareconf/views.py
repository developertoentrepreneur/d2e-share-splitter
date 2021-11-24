from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic import View

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.shareconf.models import ShareConfiguration
from d2e_share_splitter.shareconf.utils import update_pie_slices

# from shareusers.models import UserPie


class PieView(LoginRequiredMixin, TemplateView):
    template_name = "shareconf/shareconf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_pie_slices()
        context["shareconf"] = ShareConfiguration.objects.all()
        context["projects"] = Project.objects.all()
        # context["users"] = UserPie.objects.all()
        return context


class CreateProj(View):
    def get(self, request):
        name1 = request.GET.get("name", None)
        obj = Project.objects.create(name=name1)
        proj = {"id": obj.id, "name": obj.name}
        data = {"proj": proj}
        return JsonResponse(data)


class DeleteProj(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        obj = Project.objects.get(id=id1)
        obj.delete()
        data = {"deleted": True}
        return JsonResponse(data)
