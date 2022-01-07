import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from d2e_share_splitter.shareconf.factories import ProjectFactory
from d2e_share_splitter.users.utils import create_admin_user

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Populate db with factory data"

    def handle(self, *args, **options):
        admin = create_admin_user()
        project = ProjectFactory(name="Pecunia")
