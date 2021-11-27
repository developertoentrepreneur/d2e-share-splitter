import pytest
from rest_framework.test import APIClient

from d2e_share_splitter.users.models import User
from d2e_share_splitter.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture()
def api_client():
    print("\nCREATE SESSION FIXTURE : client")
    return APIClient()
