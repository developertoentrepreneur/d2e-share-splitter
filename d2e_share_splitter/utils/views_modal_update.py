from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.generics import RetrieveUpdateAPIView
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
