from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from d2e_share_splitter.users.models import User

from .serializers import UserFormSerializer
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = "atoms/modals/modal_update.html"
    queryset = User.objects.all()
    serializer_class = UserFormSerializer
    lookup_url_kwarg = "user_pk"

    def get(self, request, user_pk):
        user: User = get_object_or_404(User, pk=user_pk)
        response = {
            "user": user,
            "serializer": self.get_serializer(user),
            "url_edit": reverse("users:form", kwargs={"user_pk": user.pk}),
            "title": f"Update user {user.username}",
        }
        return Response(response)

    def post(self, request, *args, **kwargs):
        # the requests should be a patch, but since forms only
        # allow get or post, we must accept the post method
        self.partial_update(request, *args, **kwargs)
        return redirect(reverse("users:list_users"))
