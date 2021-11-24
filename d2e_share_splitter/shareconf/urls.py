from django.urls import path

from d2e_share_splitter.shareconf import views

app_name = "shareconf"

urlpatterns = [
    # Django Ajax CRUD Operations
    path("", views.PieView.as_view(), name="pie_conf"),
    path("proj/create/", views.CreateProj.as_view(), name="proj_create"),
    path("proj/delete/", views.DeleteProj.as_view(), name="proj_delete"),
]
