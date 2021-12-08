from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.edit import CreateView

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.forms import FormCreateContribution
from d2e_share_splitter.sharecontributions.models import ContribLog
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.users.models import User


class ContribsView(LoginRequiredMixin, ListView):
    model = Contribution
    template_name = "sharecontributions/contributions_list.html"
    paginate_by = 2
    context_object_name = "contributions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shareusers"] = User.objects.all()
        context["projects"] = Project.objects.all()
        context["form"] = FormCreateContribution
        return context


# Create your views here.
class ContribLog(LoginRequiredMixin, ListView):
    """docstring forBacktestList."""

    template_name = "sharecontributions/contriblog.html"
    model = ContribLog


class CreateContrib(CreateView):
    model = Contribution
    success_url = reverse_lazy("sharecontributions:list_contribs")
    form_class = FormCreateContribution


class DeleteContrib(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        obj = Contribution.objects.get(id=id1)
        # createLog(str(obj.name), "delete", "Contrib deleted")
        obj.delete()

        try:
            user = User.objects.get(name=obj.user)
            user.slices = user.slices - obj.slices
            user.save()
        except:
            pass

        data = {"deleted": True}

        return JsonResponse(data)
