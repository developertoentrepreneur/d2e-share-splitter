from django.urls import reverse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.utils.views_modal import ModalRetrieveUpdateView
