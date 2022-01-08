from django import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.forms import FormCreateContribution
from d2e_share_splitter.sharecontributions.forms import (
    fields_form_shareconribution,
)  # NOQA
from d2e_share_splitter.sharecontributions.models import ContribLog
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.sharecontributions.utils import (
    compute_contrib_pie_shares,
)  # NOQA
from d2e_share_splitter.users.models import User
from d2e_share_splitter.utils.views_modal import ListPaginatedWithFormView


class ContribsView(LoginRequiredMixin, ListPaginatedWithFormView):
    model = Contribution
    template_name = "sharecontributions/contributions_list.html"
    context_object_name = "contributions"
    form_class = FormCreateContribution
    ordering = ["-date"]


class ContribLog(LoginRequiredMixin, ListView):
    """docstring forBacktestList."""

    template_name = "sharecontributions/contriblog.html"
    model = ContribLog


class CreateContrib(CreateView):
    model = Contribution
    fields = fields_form_shareconribution
    template_name = "sharecontributions/contributions_list.html"
    success_url = reverse_lazy("sharecontributions:list_contribs")

    def form_valid(self, form):
        self.object = form.save()
        compute_contrib_pie_shares(self.object)
        return HttpResponseRedirect(self.get_success_url())


class DeleteContrib(View):
    model = Contribution
    success_url = reverse_lazy("sharecontributions:list_contribs")


class UpdateContribFormView(View):
    def post(self, request, *args, **kwargs):
        form = FormCreateContribution(data=request.POST)
        return render(request, "atoms/crispy_form.html", {"form": form})
