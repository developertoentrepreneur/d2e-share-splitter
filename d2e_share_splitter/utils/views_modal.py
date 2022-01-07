from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.list import ListView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer


class ModalRetrieveUpdateView(RetrieveUpdateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = "atoms/modals/modal_update.html"

    def post(self, request, *args, **kwargs):
        # the requests should be a patch, but since forms only
        # allow get or post, we must accept the post method
        self.partial_update(request, *args, **kwargs)
        return redirect(reverse(self.redirect_url))


class ListPaginatedWithFormView(ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context
