from django.urls import path

from d2e_share_splitter.sharecontributions import views

app_name = "sharecontributions"

urlpatterns = [
    # Django Ajax CRUD Operations
    path("contribs/", views.ContribsView.as_view(), name="list_contribs"),
    # path('contribs/log', views.ContribsLog.as_view(), name='log_contribs'),
    path("contribs/create/", views.CreateContrib.as_view(), name="contrib_create"),
    path(
        "contrib/<int:pk>/delete/",
        views.DeleteContrib.as_view(),
        name="contrib_delete",
    ),
    path(
        "contrib/update-form/",
        views.UpdateContribFormView.as_view(),
        name="contrib_form_update",
    ),
]
