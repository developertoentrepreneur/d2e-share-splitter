import pytest
from django.test import RequestFactory
from django.urls import reverse

from d2e_share_splitter.users.api.views import UserViewSet
from d2e_share_splitter.users.models import User
from d2e_share_splitter.users.tests.factories import UserFactory
from d2e_share_splitter.users.tests.factories import UserPieFactory
from d2e_share_splitter.users.utils import create_admin_user

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
    def test_get_auth_token(self, api_client):
        user = UserFactory(username="alvaro", password="Qwertyui")
        url = reverse("auth-token")
        data = {"username": user.username, "password": "Qwertyui"}
        response = api_client.post(url, data)
        assert "token" in response.data.keys()

    def test_get_queryset(self, api_client, user):
        user_pie = UserPieFactory()
        url = reverse("users:retrieve-update", kwargs={"user_pk": user_pie.pk})
        api_client.force_authenticate(user)
        response = api_client.get(url)
        data_keys = response.data.keys()
        assert "name" in data_keys
        assert "jobTitle" in data_keys
        assert "email" in data_keys
        assert "yearSalary" in data_keys

    def test_update_user_pie(self, api_client, user):
        params = {"name": "Pedro"}
        user_pie = UserPieFactory()
        url = reverse("users:retrieve-update", kwargs={"user_pk": user_pie.pk})
        api_client.force_authenticate(user)
        response = api_client.patch(url, params)
        assert response.status_code == 200
        user_pie.refresh_from_db()
        assert user_pie.name == params.get("name")
