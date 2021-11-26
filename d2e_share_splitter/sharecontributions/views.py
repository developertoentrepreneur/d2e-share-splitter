from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import View

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.shareconf.models import ShareConfiguration
from d2e_share_splitter.sharecontributions.models import ContribLog
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.users.models import UserPie


class ContribsView(LoginRequiredMixin, TemplateView):
    template_name = "sharecontributions/contributions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contributions"] = Contribution.objects.all()
        context["shareusers"] = UserPie.objects.all()
        context["projects"] = Project.objects.all()
        return context


# Create your views here.
class ContribLog(LoginRequiredMixin, ListView):
    """docstring forBacktestList."""

    template_name = "sharecontributions/contriblog.html"
    model = ContribLog


class CreateContrib(View):
    def get(self, request):
        date = request.GET.get("date", None)
        user = request.GET.get("user", None)
        contribType = request.GET.get("contribType", None)
        projectType = request.GET.get("projectType", None)
        expenses = float(request.GET.get("expenses", None))
        details = request.GET.get("description", None)
        hours = float(request.GET.get("hours", None))

        computed = compute_pie_slices(user, expenses, hours)
        print(computed["slices"], computed["value"])
        print("details: " + details)
        obj = Contribution.objects.create(
            user=user,
            contribType=contribType,
            projectType=projectType,
            value=computed["value"],
            hours=hours,
            date=date,
            details=details,
            slices=computed["slices"],
        )
        # createLog(name1, "new", "New contrib")

        contrib = {
            "user": obj.user,
            "contribType": obj.contribType,
            "projectType": obj.projectType,
            "value": obj.value,
            "hours": obj.hours,
            "date": obj.date,
            "details": obj.details,
            "slices": obj.slices,
        }

        data = {"contrib": contrib}
        return JsonResponse(data)


class DeleteContrib(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        obj = Contribution.objects.get(id=id1)
        # createLog(str(obj.name), "delete", "Contrib deleted")
        obj.delete()

        try:
            user = UserPie.objects.get(name=obj.user)
            user.slices = user.slices - obj.slices
            user.save()
        except:
            pass

        data = {"deleted": True}

        return JsonResponse(data)


# def createLog(contrib, type, details):
#     print(contrib)
#     obj = ContribLog.objects.create(date=datetime.datetime.now(),
#                                  type=type,
#                                  contrib=contrib,
#                                  details=details
#                                  )
#     obj.save()


def compute_pie_slices(
    name,
    expenses=0,
    hours=None,
):
    shareconf = ShareConfiguration.objects.get(pk=1)
    user = UserPie.objects.get(name=name)
    if hours != 0:
        print("in hours: " + str(hours))
        hourly_rate = user.yearSalary / 2000  # since it's considered 2000h/year
        value = hours * hourly_rate
        slices = value * shareconf.nonCashMultiplier
        print(
            "slices: "
            + str(slices)
            + ", hourlyrate: "
            + str(hourly_rate)
            + ", expenses: "
            + str(expenses)
            + ", Noncash: "
            + str(shareconf.nonCashMultiplier)
            + ", value: "
            + str(value)
        )
    elif expenses != 0:
        value = expenses
        slices = value * shareconf.cashMultiplier

    user.slices = user.slices + slices
    user.save()

    return {"slices": round(slices, 2), "value": round(value, 2)}
