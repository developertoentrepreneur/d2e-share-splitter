from django.urls import path

from d2e_share_splitter.users.api.views import UserRetrieveUpdateView
from d2e_share_splitter.users.views import CreateUser
from d2e_share_splitter.users.views import DeleteUser
from d2e_share_splitter.users.views import UpdateUser
from d2e_share_splitter.users.views import UserDetailView
from d2e_share_splitter.users.views import UserRedirectView
from d2e_share_splitter.users.views import UsersLog
from d2e_share_splitter.users.views import UsersView
from d2e_share_splitter.users.views import UserUpdateView

app_name = "users"
urlpatterns_view = [
    path("list/", UsersView.as_view(), name="list_users"),
    path("log/", UsersLog.as_view(), name="log_users"),
    path("create/", CreateUser.as_view(), name="user_create"),
    path("delete/", DeleteUser.as_view(), name="user_delete"),
    path("update/", UpdateUser.as_view(), name="user_update"),
    path("~redirect/", UserRedirectView.as_view(), name="redirect"),
    path("~update/", UserUpdateView.as_view(), name="update"),
    path("<str:username>/", UserDetailView.as_view(), name="detail"),
    # Django Ajax CRUD Operations
]

urlpatterns_api = [
    path(
        "pie/<int:user_pk>/",
        UserRetrieveUpdateView.as_view(),
        name="form",
    ),
]

urlpatterns = urlpatterns_view + urlpatterns_api
