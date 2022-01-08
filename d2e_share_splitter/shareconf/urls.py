from django.urls import path

from d2e_share_splitter.shareconf import views
from d2e_share_splitter.shareconf.api.views import ProjectRetrieveUpdateView

app_name = "shareconf"

urlpatterns_view = [
    # Django Ajax CRUD Operations
    path("", views.ShareDistributionView.as_view(), name="pie_conf"),
    path("proj/create/", views.CreateProj.as_view(), name="proj_create"),
    path("proj/<int:pk>/delete/", views.DeleteProj.as_view(), name="proj_delete"),
]


urlpatterns_api = [
    path(
        "pie/<int:project_pk>/",
        ProjectRetrieveUpdateView.as_view(),
        name="form",
    ),
]

urlpatterns = urlpatterns_view + urlpatterns_api
