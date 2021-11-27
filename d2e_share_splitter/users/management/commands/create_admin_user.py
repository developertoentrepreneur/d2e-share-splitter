import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from d2e_share_splitter.users.utils import create_admin_user

logger = logging.getLogger(__name__)
from d2e_share_splitter.users.tests.factories import TokenUserFactory


class Command(BaseCommand):

    help = "Update to new values"

    def handle(self, *args, **options):
        return create_admin_user()
