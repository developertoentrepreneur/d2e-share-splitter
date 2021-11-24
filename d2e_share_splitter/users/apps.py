from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "d2e_share_splitter.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import d2e_share_splitter.users.signals  # noqa F401
        except ImportError:
            pass
