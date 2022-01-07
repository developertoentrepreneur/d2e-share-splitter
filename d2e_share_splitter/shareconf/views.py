from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from d2e_share_splitter.shareconf.forms import FormCreateProject
from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.users.models import User


class ShareDistributionView(LoginRequiredMixin, ListView):
    template_name = "shareconf/shareconf.html"
    model = Project
    paginate_by = 10
    context_object_name = "projects"
    order_by = "name"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormCreateProject()
        context["users"] = User.objects.all()
        return context


class CreateProj(CreateView):
    model = Project
    fields = ["name"]
    success_url = reverse_lazy("shareconf:pie_conf")


class DeleteProj(DeleteView):
    model = Project
    success_url = reverse_lazy("shareconf:pie_conf")
