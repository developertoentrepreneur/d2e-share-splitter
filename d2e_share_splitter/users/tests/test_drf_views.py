import pytest
from django.test import RequestFactory
from django.urls import reverse

from d2e_share_splitter.users.api.views import UserViewSet
from d2e_share_splitter.users.models import User
from d2e_share_splitter.users.tests.factories import UserFactory
from d2e_share_splitter.users.tests.factories import UserPieFactory

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "name": user.name,
            "url": f"http://testserver/api/users/{user.username}/",
        }


class TestUserViewSet:
    def test_get_queryset(self, api_client, user):

        user = UserPieFactory()
        url = reverse("users:retrieve-update", kwargs={"user_pk": user.pk})
        api_client.force_authenticate(user)
        response = api_client.get(url)
        import ipdb

        ipdb.set_trace()

        assert response.data == {"hello": "hi"}
