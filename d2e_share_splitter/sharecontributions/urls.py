from sharecontributions import views
from django.urls import path


app_name = "sharecontributions"

urlpatterns = [
    # Django Ajax CRUD Operations
    path("contribs/", views.ContribsView.as_view(), name="list_contribs"),
    # path('contribs/log', views.ContribsLog.as_view(), name='log_contribs'),
    path("contribs/create/", views.CreateContrib.as_view(), name="contrib_create"),
    path("contrib/delete/", views.DeleteContrib.as_view(), name="contrib_delete"),
    # path('contrib/update/', views.UpdateContrib.as_view(), name='contrib_update'),
]
