from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from d2e_share_splitter.users.forms import FormUser

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.request.user.username}
        )


user_redirect_view = UserRedirectView.as_view()


import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.edit import CreateView

from d2e_share_splitter.users.models import UserLog
from d2e_share_splitter.users.models import UserPie


# Create your views here.
class UsersLog(LoginRequiredMixin, ListView):
    """docstring forBacktestList."""

    template_name = "users/userslog.html"
    model = UserLog


class UsersView(LoginRequiredMixin, TemplateView):
    template_name = "users/userslist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserPie.objects.all()
        context["form"] = FormUser()
        return context


class CreateUser(CreateView):
    model = UserPie
    fields = ["name", "email", "jobTitle", "yearSalary"]

    def get(self, request):
        name1 = request.GET.get("name", None)
        email1 = request.GET.get("email", None)
        jobTitle1 = request.GET.get("jobTitle", None)
        yearSalary1 = request.GET.get("yearSalary", None)

        obj = UserPie.objects.create(
            name=name1, email=email1, jobTitle=jobTitle1, yearSalary=yearSalary1
        )
        createLog(name1, "new", "New user")

        user = {
            "id": obj.id,
            "name": obj.name,
            "email": obj.email,
            "jobTitle": obj.jobTitle,
            "yearSalary": obj.yearSalary,
        }

        data = {"user": user}
        return JsonResponse(data)


class DeleteUser(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        obj = UserPie.objects.get(id=id1)
        createLog(str(obj.name), "delete", "User deleted")
        obj.delete()
        data = {"deleted": True}

        return JsonResponse(data)


class UpdateUser(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        name1 = request.GET.get("name", None)
        email1 = request.GET.get("email", None)
        jobTitle1 = request.GET.get("jobTitle", None)
        yearSalary1 = request.GET.get("yearSalary", None)

        obj = UserPie.objects.get(id=id1)
        details = checkEdit(
            [name1, email1, jobTitle1, yearSalary1],
            [obj.name, obj.email, obj.jobTitle, obj.yearSalary],
        )
        createLog(str(obj.name), "edit", details)
        obj.name = name1
        obj.email = email1
        obj.jobTitle = jobTitle1
        obj.yearSalary = yearSalary1
        obj.save()

        user = {
            "id": obj.id,
            "name": obj.name,
            "email": obj.email,
            "jobTitle": obj.jobTitle,
            "yearSalary": obj.yearSalary,
        }

        data = {"user": user}
        return JsonResponse(data)


def createLog(user, type, details):
    print(user)
    obj = UserLog.objects.create(
        date=datetime.datetime.now(), type=type, user=user, details=details
    )
    obj.save()


def checkEdit(new_values, old_values):
    i = 0
    details = ""
    for item in new_values:
        if item != old_values[i]:
            change = (
                "Old: " + str(old_values[i]) + ", new: " + str(item) + "\n --"
            )
            details = details + change
        i = i + 1
    return details
